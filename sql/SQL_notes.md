# SQL notes

---

## 11/18/2025

I forgot about time constraint.

---

## 11/19/2025

When using filters on results after groupby, you need to use HAVING.

---

## 12/02/2025

I learned about EXCEPT

Using the EXCEPT operator, we subtract the page IDs with likes from the initial set of all page IDs. The resulting query will give us the IDs of the Facebook pages that do not possess any likes.

```sql
SELECT page_id
FROM pages
EXCEPT
SELECT page_id
FROM page_likes
ORDER BY page_id;
```

---

## 12/07/2025

1. Even though the query is written top-down, SQL actually runs bottom-up according to this logical order:  
   **FROM, WHERE, GROUP BY, HAVING, SELECT**

2. `DATE_PART('year', post_date::DATE) = 2021`  
   `post_date::DATE` casts the timestamp to a date.
   - Removes the time component.
   - Example: 2021-07-10 12:00:00 → 2021-07-10  
   `DATE_PART('year', ...)` extracts the year from the date.  
   Or `EXTRACT(YEAR FROM post_date)`

3. **DATE_TRUNC** truncates a timestamp or date to a specified precision by setting all lower-order units to zero (or the first day).  
   `DATE_TRUNC('month', '2022-08-03 15:20:40')`  
   Output: 2022-08-01 00:00:00

---

## 12/09/25

Assume you're given the tables containing **completed** trade orders and user details in a Robinhood trading system.

Write a query to retrieve the top three cities that have the highest number of completed trade orders listed in descending order. Output the city name and the corresponding number of completed trade orders.

```sql
SELECT users.city AS city, COUNT(DISTINCT trades.order_id) AS total_orders
FROM trades
LEFT JOIN users ON trades.user_id = users.user_id
WHERE trades.status = 'Completed'
GROUP BY users.city
ORDER BY COUNT(DISTINCT trades.order_id) DESC
LIMIT 3;
```

I forgot the filter 'Completed'

---

## 12/10/25

```sql
SELECT DATE_PART('month', submit_date::DATE) AS mth,
       product_id AS product,
       ROUND(AVG(stars), 2) AS avg_stars
FROM reviews
GROUP BY product_id, DATE_PART('month', submit_date::DATE)
ORDER BY DATE_PART('month', submit_date::DATE), product_id;
```

`ORDER BY DATE_PART('month', submit_date::DATE)` can be replaced by `ORDER BY mth` because it has been defined previously.

| Join type       | Behavior |
|-----------------|----------|
| **INNER JOIN**  | Returns only the rows with matching values from both tables. |
| **LEFT JOIN**   | Returns all the rows from the left table and the matching rows from the right table. |
| **RIGHT JOIN**  | Returns all the rows from the right table and the matching rows from the left table. |
| **FULL OUTER JOIN** | Returns all rows when there is a match in either the left or the right table. If no match, NULL values are returned for columns from the table without a match. |

---

## 12/17/25

`CASE WHEN ... THEN ... ELSE ... END`

---

## 01/07/26

To compute a row-level calculation in SQL, both values must be available in the same row context, typically as columns or derived expressions.

**Example:** Assume you have an events table on Facebook app analytics. Write a query to calculate the click-through rate (CTR) for the app in 2022 and round the results to 2 decimal places.

**Percentage of click-through rate (CTR) = 100.0 * Number of clicks / Number of impressions**

To avoid integer division, multiply the CTR by 100.0, not 100.

**events Table:**  
Column Name | Type  
app_id | integer  
event_type | string  
timestamp | datetime  

Here you need to first make two new columns, impression and click, then you do operations over these two new columns.

---

## 01/15/2026

To write a condition where two datetime has gaps:

- `action_date = signup_date + INTERVAL '1 day';`
- `action_date = signup_date + INTERVAL '1 week';`
- `action_date = signup_date + INTERVAL '1 month';`
- `action_date = signup_date + INTERVAL '1 year';`

---

## 02/06/2026

**WHERE** is applied after the **LEFT JOIN**—it filters rows from the result set, not from the joined table. If you want to only filter from one of the tables in the joining operation, you should just use **AND**.

https://datalemur.com/questions/sql-ibm-db2-product-analytics

**BETWEEN start AND end:** `>= start AND <= end`

- `BETWEEN '2023-07-01' AND '2023-09-30'` includes the full day of September 30, but no time is specified.
- In most SQL implementations, `'2023-09-30'` is interpreted as `'2023-09-30 00:00:00'`.
- So any queries later in the day on Sep 30 (e.g., `'2023-09-30 14:00:00'`) are excluded.

---

## 02/07/2026

`RANK() OVER (PARTITION BY x ORDER BY y)` — generate a ranking column from an existing column.

The **CASE** statement in the **WHERE** clause is used to filter **rows** based on specified conditions within the dataset.

**Mistake I made today:**  
Write a query to find the top 3 most profitable drugs sold, and how much profit they made. Assume that there are no ties in the profits.  
I used unit profit instead total profit for ranking. I guess it's helpful to ask the interviewer which metrics to use.

- WHERE runs before aggregation. You cannot do `WHERE COUNT(x) > 3`
- WHERE runs after join

---

## 02/09/2026

`ROWS BETWEEN 2 PRECEDING AND CURRENT ROW`

`ORDER BY department_name ASC, salary DESC, name ASC`  
I made the mistake to only order by two conditions.

In a **LEFT JOIN**, the **AND** in the **ON** clause only filters table t (the right table), not the left one.

- **UNION ALL** keeps everything, including duplicates.
- **UNION** removes duplicates, so you get only the unique items.

---

## 02/10/2026

`SUM(CASE WHEN rank % 2 != 0 THEN measurement_value END) AS odd_sum`  
Operations like SUM, AVG should happen first, and END should be in the parenthesis. AS should be right after parenthesis.

---

## 02/11/2026

```sql
CASE
    WHEN order_id = (SELECT MAX(order_id) FROM orders) AND order_id % 2 != 0 THEN order_id
    WHEN order_id % 2 = 0 THEN order_id - 1
    ELSE order_id + 1
END AS ...
```

I did not remember the syntax; also CASE does not always need an ELSE.

When you want to combine two columns from two different tables, use `WITH x AS ..., y AS ...`, then do a SELECT in the end.

`DATE(T2.transaction_date) = DATE(T1.transaction_date) + 1`  
equals  
`transaction_date + INTERVAL '1 day' AS transaction_date`

To make two date columns like year and month into one date column, use `MAKE_DATE(issue_year, issue_month, 1)`.

**COUNT(column) does NOT count NULL values!!!**

## 03/05/2026

- Within WHERE clause, SQL does not execute top down.
```sql
WHERE 
EXTRACT(YEAR FROM curr_month.event_date) = 2022
AND EXTRACT(MONTH FROM curr_month.event_date) = 7
```
and 
```sql
WHERE 
EXTRACT(MONTH FROM curr_month.event_date) = 7
AND EXTRACT(YEAR FROM curr_month.event_date) = 2022
```
are the same


- Learned lag()

https://datalemur.com/questions/yoy-growth-rate

Usually used when you see
year-over-year
month-over-month
previous value


## 03/09/2025

- Big table

When the original table is large, JOIN is generally more efficient, because it focuses on the subset of rows that matter

- Window functions

Key Rule: Window Functions cannot be in WHERE

- Division rule

If both numbers in a division are integers → SQL returns an integer.
If at least one number is a decimal/float → SQL returns a decimal.
Solution: COUNT(user_id) * 1.0 / COUNT(total_users)