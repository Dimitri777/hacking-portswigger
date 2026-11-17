# Cross-origin resource sharing (CORS) - PortSwigger Web Security Academy

Solutions for the CORS labs in the CORS topic.

All of these abuse a server that reflects/trusts the request `Origin` while also
sending `Access-Control-Allow-Credentials: true`, so a cross-origin page can read
an authenticated response (the victim's `/accountDetails`, which contains their API key).

## Labs

### Apprentice
1. [CORS vulnerability with basic origin reflection](01-basic-origin-reflection.md)
2. [CORS vulnerability with trusted null origin](02-trusted-null-origin.md)

### Practitioner
3. [CORS vulnerability with trusted insecure protocols](03-trusted-insecure-protocols.md)

Replace `YOUR-LAB-ID` with your lab's hostname and `YOUR-EXPLOIT-SERVER-ID` with your
exploit server's hostname. Log in to each lab as `wiener:peter` first, then host the
payload on the exploit server and "Deliver exploit to victim". The administrator's API
key lands in the exploit server **Access log**; submit it with "Submit solution".
