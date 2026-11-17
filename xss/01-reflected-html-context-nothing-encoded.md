# Lab: Reflected XSS into HTML context with nothing encoded (Apprentice)

**Lab:** [https://portswigger.net/web-security/cross-site-scripting/reflected/lab-html-context-nothing-encoded](https://portswigger.net/web-security/cross-site-scripting/reflected/lab-html-context-nothing-encoded)

**Task (from PortSwigger):**
This lab contains a simple reflected cross-site scripting vulnerability in the search
functionality. To solve the lab, perform a cross-site scripting attack that calls the
`alert` function.

## Vulnerability
The search term is reflected straight into the HTML response with no encoding or filtering.

## Solution
Enter this in the search box (or as the `search` query parameter) and submit:

```html
<script>alert(1)</script>
```

The script is reflected into the page and executes, firing the alert. Lab solved.
