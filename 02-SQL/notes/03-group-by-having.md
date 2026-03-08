# GROUP BY, HAVING, Aggregate Functions

## Aggregate Functions
```sql
SELECT COUNT(*), SUM(salary), AVG(salary), MIN(salary), MAX(salary)
FROM employees;
```

## GROUP BY
```sql
SELECT department, COUNT(*) as emp_count, AVG(salary) as avg_salary
FROM employees
GROUP BY department;
```

## HAVING (filter after grouping)
```sql
SELECT department, COUNT(*) as emp_count
FROM employees
GROUP BY department
HAVING COUNT(*) > 5;
```

## Execution Order
```
FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY -> LIMIT
```

## Notes
<!-- Add your notes here as you learn -->
