# Lab: SQL injection with filter bypass via XML encoding (Practitioner)

**Goal:** Bypass WAF/filter that blocks common SQL keywords by encoding the payload in XML entities or similar.

## Technique

The application accepts XML input. Encode the SQL payload using XML character entities so that the filter does not see the keywords, but the backend still executes them after decoding.

## Example Approach

Submit a payload where SQL keywords are replaced by XML entities:

```xml
&#x53;ELECT ...   (S = &#x53;)
```

Or full payload encoded.

Typical successful payload structure involves injecting into an XML parameter with encoded `UNION SELECT` etc.

Refer to the lab for the exact injection point (usually a stock check or similar XML endpoint).
