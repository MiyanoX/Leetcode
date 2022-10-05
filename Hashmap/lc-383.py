class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
		# create new hash map
        d = {}
        for char in magazine:
            if char not in d:
                d[char] = 1
            else:
                d[char] += 1
       
		# find if ransom note can be constructed within hashmap
        for char in ransomNote:
            if char not in d or d[char] == 0:
                return False
            d[char] -= 1
            
        return True