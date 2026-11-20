# Lab: File path traversal, traversal sequences blocked with absolute path bypass (Practitioner)

**Lab:** [https://portswigger.net/web-security/file-path-traversal/lab-absolute-path-bypass](https://portswigger.net/web-security/file-path-traversal/lab-absolute-path-bypass)

**Task (from PortSwigger):**  
This lab contains a path traversal vulnerability in the display of product images.

The application blocks traversal sequences but treats the supplied filename as being relative to a default working directory.

To solve the lab, retrieve the contents of the `/etc/passwd` file.

## Vulnerability
`../` is blocked, but an absolute path is accepted and resolved from the filesystem root (or treated relative to a working directory that still allows absolute paths).

## Solution

```
filename=/etc/passwd
```

## Final Payload
```
/etc/passwd
```
