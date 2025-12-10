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