11/18/2025
I forgot about time constraint.

11/19/2025
When using filters on results after groupby, you need to us HAVING.

12/02/2025
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