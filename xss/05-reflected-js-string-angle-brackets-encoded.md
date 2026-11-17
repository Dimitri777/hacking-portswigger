# Lab: Reflected XSS into a JavaScript string with angle brackets HTML encoded (Practitioner)

**Lab:** [https://portswigger.net/web-security/cross-site-scripting/contexts/lab-javascript-string-angle-brackets-html-encoded](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-javascript-string-angle-brackets-html-encoded)

**Task (from PortSwigger):**
This lab contains a reflected cross-site scripting vulnerability in the search query
tracking functionality where angle brackets are HTML encoded. To solve the lab, perform a
cross-site scripting attack that breaks out of the JavaScript string and calls the
`alert` function.

## Vulnerability
The search term is reflected inside a JavaScript string literal. Angle brackets are HTML
encoded (so you cannot inject a new tag), but quotes are not, so you can break out of the
string and inject JavaScript expressions directly.

## Solution
Enter this in the search box (or as the `search` query parameter):

```js
'-alert(1)-'
```

This closes the string, evaluates `alert(1)` as part of the expression, and reopens the
string, firing the alert. Lab solved.
