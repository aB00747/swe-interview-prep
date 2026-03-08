# Subqueries & CTEs

## Subquery in WHERE
```sql
SELECT * FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

SELECT * FROM employees
WHERE dept_id IN (SELECT id FROM departments WHERE location = 'NYC');
```

## Subquery in FROM (Derived Table)
```sql
SELECT dept, avg_sal FROM (
    SELECT department AS dept, AVG(salary) AS avg_sal
    FROM employees GROUP BY department
) AS dept_avg
WHERE avg_sal > 60000;
```

## CTE (Common Table Expression)
```sql
WITH dept_avg AS (
    SELECT department, AVG(salary) AS avg_salary
    FROM employees
    GROUP BY department
)
SELECT * FROM dept_avg WHERE avg_salary > 60000;
```

## Correlated Subquery
```sql
SELECT e.name, e.salary FROM employees e
WHERE e.salary > (
    SELECT AVG(salary) FROM employees WHERE department = e.department
);
```

## Notes
<!-- Add your notes here as you learn -->
