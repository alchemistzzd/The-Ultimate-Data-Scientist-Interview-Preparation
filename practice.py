def lengthOfLongestSubstring(s: str) -> int:
    if len(s) == 0:
            return 0
    max_leng = 1
    left_pointer = 0
    right_pointer = 0
    ele_dict = {s[0]:0}
        
    for i in range(1,len(s)):
        if s[i] not in ele_dict.keys():
            right_pointer +=1
            ele_dict[s[i]] = i
            max_leng = max(max_leng, (right_pointer - left_pointer+1))
        else:
            if ele_dict[s[i]]+1 == i:
                right_pointer +=1
                ele_dict[s[i]] = i
                left_pointer = max(left_pointer, ele_dict[s[i]] + 1)
                max_leng = max(max_leng, (right_pointer - left_pointer+1))
            else:
                right_pointer +=1
                ele_dict[s[i]] = i
                left_pointer = max(left_pointer, ele_dict[s[i]] + 1)
                max_leng = max(max_leng, (right_pointer - left_pointer+1))
    return max_leng

result = lengthOfLongestSubstring("thequickbrownfoxjumpsoverthelazydogthequickbrownfoxjumpsovert")
print(result)