# Lab: Stored XSS into HTML context with nothing encoded (Apprentice)

**Lab:** [https://portswigger.net/web-security/cross-site-scripting/stored/lab-stored-html-context-nothing-encoded](https://portswigger.net/web-security/cross-site-scripting/stored/lab-stored-html-context-nothing-encoded)

**Task (from PortSwigger):**
This lab contains a stored cross-site scripting vulnerability in the comment
functionality. To solve the lab, submit a comment that calls the `alert` function when
the blog post is viewed.

## Vulnerability
A blog comment is stored and later rendered into the post page without any encoding.

## Solution
Open a blog post, go to the comment form, and submit a comment with this body (fill the
other required fields, e.g. Name/Email/Website, with any valid values):

```html
<script>alert(1)</script>
```

Reload the blog post; the stored script runs for anyone viewing it, firing the alert.
Lab solved.
