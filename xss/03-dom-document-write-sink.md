# Lab: DOM XSS in document.write sink using source location.search (Apprentice)

**Lab:** [https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-document-write-sink](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-document-write-sink)

**Task (from PortSwigger):**
This lab contains a DOM-based cross-site scripting vulnerability in the search query
tracking functionality. It uses the JavaScript `document.write` function, which writes
data out to the page. The `document.write` function is called with data from
`location.search`, which you can control using the website URL. To solve the lab, perform
a cross-site scripting attack that calls the `alert` function.

## Vulnerability
The search term from `location.search` is passed to `document.write`, which builds an
`<img src="...SEARCH...">` tag. Breaking out of the `src` attribute injects a new element.

## Solution
Enter this in the search box (or as the `search` query parameter):

```html
"><svg onload=alert(1)>
```

This closes the `img src` attribute/tag and injects an `<svg onload>` that fires the
alert. Lab solved.
