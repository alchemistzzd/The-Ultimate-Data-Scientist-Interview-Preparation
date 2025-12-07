Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
```python
def longest_consecutive_sequence(nums):
    maxlength = 1
    # hashmap = {item: True for item in nums}
    for i in nums:
        if (i-1) not in nums:
            leng = 1
            while (i+leng) in nums:
                leng += 1
            maxlength = max(maxlength, leng)
        
    # Replace this placeholder return statement with your code
    
    return maxlength
```
Notes:
1. Sort the array works but it is nlogn
2. Scan the array and check if i-1 is in, if it is not in then i is the starting of an array. Then check i+1, i+2...and record the length.

To be implemented: https://www.youtube.com/watch?v=HgV209w2iu8