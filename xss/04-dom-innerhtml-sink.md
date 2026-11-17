# Lab: DOM XSS in innerHTML sink using source location.search (Apprentice)

**Lab:** [https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-innerhtml-sink](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-innerhtml-sink)

**Task (from PortSwigger):**
This lab contains a DOM-based cross-site scripting vulnerability in the search blog
functionality. It uses an `innerHTML` assignment, which changes the HTML contents of a
`div` element, using data from `location.search`. To solve the lab, perform a cross-site
scripting attack that calls the `alert` function.

## Vulnerability
The search term is assigned to an element's `innerHTML`. `innerHTML` ignores `<script>`
tags, so use an element with an event handler instead.

## Solution
Enter this in the search box (or as the `search` query parameter):

```html
<img src=1 onerror=alert(1)>
```

The broken image triggers `onerror`, which fires the alert. Lab solved.
