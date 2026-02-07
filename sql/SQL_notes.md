## 11/18/2025
I forgot about time constraint.

## 11/19/2025
When using filters on results after groupby, you need to use HAVING.

## 12/02/2025
I learned about EXCEPT

Using the EXCEPT operator, we subtract the page IDs with likes from the initial set of all page IDs. The resulting query will give us the IDs of the Facebook pages that do not possess any likes.
```sql
SELECT page_id
FROM pages
EXCEPT
SELECT page_id
FROM page_likes
order by page_id;
```

## 12/07/2025
1. Even though the query is written top-down, SQL actually runs bottom-up according to this logical order
FROM, WHERE, GROUP BY, HAVING, SELECT

2. DATE_PART('year', post_date::DATE) = 2021 
post_date::DATE casts the timestamp to a date.
	•	Removes the time component.
	•	Example: 2021-07-10 12:00:00 → 2021-07-10
DATE_PART('year', ...) extracts the year from the date.
or EXTRACT(YEAR FROM post_date) 

3. DATE_TRUNC truncates a timestamp or date to a specified precision by setting all lower-order units to zero (or the first day).
DATE_TRUNC('month', '2022-08-03 15:20:40')
Output:2022-08-01 00:00:00

## 12/09/25
Assume you're given the tables containing **completed** trade orders and user details in a Robinhood trading system.

Write a query to retrieve the top three cities that have the highest number of completed trade orders listed in descending order. Output the city name and the corresponding number of completed trade orders.
```sql
SELECT users.city as city, count(distinct trades.order_id) as total_orders FROM trades
left join users
on trades.user_id = users.user_id
where trades.status = 'Completed'
group by users.city
order by count(distinct trades.order_id) desc
limit 3;
```
I forgot the filter 'Completed'

## 12/10/25
```sql
SELECT date_part('month',submit_date::date) as mth,
product_id as product,
round(avg(stars),2) as avg_stars
FROM reviews
group by product_id, date_part('month',submit_date::date)
order by date_part('month',submit_date::date), product_id;
```
order by date_part('month',submit_date::date) can be replaced by order by mth because it has been defined previously.

INNER JOIN: Returns only the rows with matching values from both tables.
LEFT JOIN: Returns all the rows from the left table and the matching rows from the right table.
RIGHT JOIN: Returns all the rows from the right table and the matching rows from the left table.
FULL OUTER JOIN: Returns all rows when there is a match in either the left or the right table. If there is no match, NULL values are returned for columns from the table without a match.

## 12/17/25
case when ... then ... else ... end

## 01/07/26
To compute a row-level calculation in SQL, both values must be available in the same row context, typically as columns or derived expressions.
For example:
Assume you have an events table on Facebook app analytics. Write a query to calculate the click-through rate (CTR) for the app in 2022 and round the results to 2 decimal places.

Percentage of click-through rate (CTR) = 100.0 * Number of clicks / Number of impressions
To avoid integer division, multiply the CTR by 100.0, not 100.
events Table:
Column Name	Type
app_id	integer
event_type	string
timestamp	datetime
events Example Input:
app_id	event_type	timestamp
123	impression	07/18/2022 11:36:12
123	impression	07/18/2022 11:37:12
123	click	07/18/2022 11:37:42
234	impression	07/18/2022 14:15:12
234	click	07/18/2022 14:16:12

Here you need to first make two new columns, impression and click, then you do operations over these two new columns.

## 01/15/2026
To write a condition where two datetime has gaps:
action_date = signup_date + interval '1 day';
action_date = signup_date + interval '1 week';
action_date = signup_date + interval '1 month';
action_date = signup_date + interval '1 year';


## 02/06/2026
WHERE is applied after the LEFT JOIN, it filters rows from the result set, not from the joined table. If you want to only filter from one of the table in the joining operation, you should just use and
https://datalemur.com/questions/sql-ibm-db2-product-analytics

BETWEEN start AND end:
>= start AND <= end
1.	BETWEEN '2023-07-01' AND '2023-09-30' includes the full day of September 30, but no time is specified.
•	In most SQL implementations, '2023-09-30' is interpreted as '2023-09-30 00:00:00'.
•	So any queries later in the day on Sep 30 (e.g., '2023-09-30 14:00:00') are excluded.

## 02/07/2026
rank() over(partition by x order by y)
generate a ranking column from an existing column

The CASE statement in the WHERE clause is used to filter **rows** based on specified conditions within the dataset.
