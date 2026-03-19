# SQL Examples

```sql
SELECT merchant_id, COUNT(*) AS transaction_count
FROM synthetic_transactions
GROUP BY merchant_id;
```
