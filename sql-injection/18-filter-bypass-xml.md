# Lab: SQL injection with filter bypass via XML encoding (Practitioner)

**PortSwigger:** [Official lab](https://portswigger.net/web-security/sql-injection/lab-sql-injection-with-filter-bypass-via-xml-encoding)

**Description:** Bypass a WAF in the XML-based stock-check feature, retrieve the administrator's credentials, and log in.

**Goal:** Bypass WAF/filter that blocks common SQL keywords by encoding the payload in XML entities or similar.

## Official solution summary

The official solution targets the XML-based stock-check request. It demonstrates that a filter can interpret a request differently from the component that parses and processes the XML, then uses the vulnerable query to retrieve the administrator's credentials and verify them by logging in. This summary intentionally omits bypass strings and payload construction.

## Defensive takeaways

Parse and canonicalize XML once before applying validation, reject unexpected content, and use parameterized database queries. Keep WAF inspection and backend parsing consistent; a WAF is an additional layer, not a substitute for safe query handling.
