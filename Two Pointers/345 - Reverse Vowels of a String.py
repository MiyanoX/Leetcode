class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"                               # vowels char dictionary
        start, end = 0, len(s) - 1                          # set two pointers 
        s = list(s)                                         # transform string to list
        while start < end:
            while start < end and s[start] not in vowels:   # move forward start pointer until it is vowel or end
                start += 1
            while start < end and s[end] not in vowels:     # move backward end pointer until it is vowel or start
                end -= 1
            s[start], s[end] = s[end], s[start]             # change position of start and end pointers
            start += 1
            end -= 1
        return "".join(s)                                   # transform list back o string