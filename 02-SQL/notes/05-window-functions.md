# Window Functions

## Syntax
```sql
function() OVER (
    PARTITION BY column
    ORDER BY column
    ROWS BETWEEN ... AND ...
)
```

## Ranking Functions
```sql
-- ROW_NUMBER: unique sequential number
SELECT name, salary, ROW_NUMBER() OVER (ORDER BY salary DESC) as rn FROM employees;

-- RANK: same rank for ties, skips next
SELECT name, salary, RANK() OVER (ORDER BY salary DESC) as rnk FROM employees;

-- DENSE_RANK: same rank for ties, no skip
SELECT name, salary, DENSE_RANK() OVER (ORDER BY salary DESC) as drnk FROM employees;
```

## Aggregate Window Functions
```sql
SELECT name, department, salary,
    SUM(salary) OVER (PARTITION BY department) as dept_total,
    AVG(salary) OVER (PARTITION BY department) as dept_avg
FROM employees;
```

## LAG / LEAD
```sql
SELECT name, salary,
    LAG(salary, 1) OVER (ORDER BY hire_date) as prev_salary,
    LEAD(salary, 1) OVER (ORDER BY hire_date) as next_salary
FROM employees;
```

## Notes
<!-- Add your notes here as you learn -->
