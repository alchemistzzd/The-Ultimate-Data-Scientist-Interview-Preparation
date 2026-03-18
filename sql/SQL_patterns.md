# Consecutive years

1. LAG / LEAD / window function
lag(column,1) over()
lead(column,1) over()
PARTITION BY num: if we use this we are looking at each group, so it will not catch any breaks

2. gaps-and-islands pattern
year - row_number() over() stays constant for consecutive sequences.
week - rn * interval '1 week' if dealing with timestamp data

For gap-and-island with ROW_NUMBER(), the idea is:

one sequence that numbers all rows in order

another sequence that numbers rows within a condition

## Problems:
https://datalemur.com/questions/consecutive-filing-years (didn't have order by in lag())
https://datalemur.com/questions/marketing-touch-streak
https://leetcode.com/problems/consecutive-numbers/submissions/1943181014/
https://datalemur.com/questions/user-retention
https://leetcode.com/problems/game-play-analysis-iv/
https://leetcode.com/problems/longest-winning-streak/submissions/1943329685/
https://leetcode.com/problems/consecutive-transactions-with-increasing-amounts/ - not solved


# Retention/Cohort



## Problems:
1. LeetCode (very common interview prep)

Game Play Analysis I
https://leetcode.com/problems/game-play-analysis-i/

Game Play Analysis II
https://leetcode.com/problems/game-play-analysis-ii/

Game Play Analysis III
https://leetcode.com/problems/game-play-analysis-iii/

Game Play Analysis IV
https://leetcode.com/problems/game-play-analysis-iv/

These 4 problems are the canonical retention series.

https://leetcode.com/problems/game-play-analysis-v/description/



# Top-N per group / ranking problems

https://datalemur.com/questions/sql-highest-grossing - redo



#

https://leetcode.com/problems/product-price-at-a-given-date/description/