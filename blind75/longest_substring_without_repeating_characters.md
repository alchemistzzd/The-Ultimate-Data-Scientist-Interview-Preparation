Given a string s, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        max_leng = 1
        left_pointer = 0
        ele_dict = {}

        for i in range(len(s)):
            if s[i] not in ele_dict.keys():
                ele_dict[s[i]] = i
                max_leng = max(max_leng, i-left_pointer+1)
            else:
                old_index = ele_dict[s[i]]
                left_pointer = max(left_pointer, old_index + 1)
                ele_dict[s[i]] = i
                max_leng = max(max_leng, i-left_pointer+1)
        return max_leng

Notes:
1. This is a problem to use sliding window algorithm
2. Use two pointers, right always moves 1 to the right.
3. Left pointer does not move when new element is not in the window; left pointer jumps to previous index + 1 of the new element if the new element is in the window already
4. The tricky part is if new element is not in the window but has previously appeared before. In this case left pointer should not move, new element's index needs to be updated.
5. left_pointer = max(left_pointer, old_index + 1)
This is the part that tricked me. Since old_index could be very small if the new element has already appeared before. So it is important to take the maximum of current left pointer and old_index + 1.