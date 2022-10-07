class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        start = 0
        max_length = 0
        dict = {}
        
        for i in range(len(s)):
            if s[i] not in dict:
                dict[s[i]] = i
            else:
                max_length = max(max_length, len(dict))
                end = dict[s[i]]
                for char in s[start: end]:
                    del dict[char]
                dict[s[i]] = i
                start = end + 1
        
        return max(max_length, len(dict))