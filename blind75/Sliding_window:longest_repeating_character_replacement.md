You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.

After performing at most k replacements, return the length of the longest substring which contains only one distinct character.
```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0 
        freq = {}
        max_len = 0
        for i in range(len(s)):
            # add to dict
            freq[s[i]] = freq.get(s[i],0) + 1
            # most frequent element
            top = max(freq, key = freq.get)
            top_freq = freq[top]

            window_size = i - left + 1
            
            if (window_size - top_freq) > k:
                freq[s[left]] = freq[s[left]] - 1
                left += 1
                window_size -= 1

            max_len = max(max_len, window_size)
        return max_len
```

Notes:
1. Hash map to record the most frequent element in current window
2. Check if window size - top frequent element frequency is too big for k to replace
2. When k is used up, but there are too many elements need to be replaced, move left pointer one step to the right
