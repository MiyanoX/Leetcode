class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def add(d, c):                      # help func for add item to hashmap
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
                
        def delete(d, c):                   # help func for delete item from hashmap
            if d[c] > 1:
                d[c] -= 1
            else:
                del d[c]
        
        ans = []
        
        if len(s) < len(p):                 # no anagram if p is longer than s
            return ans
        
        p_dict = {}                         # add string p to p hashmap
        for char in p:
            add(p_dict, char)
        
        s_dict = {}                         # add [0: len(p)-1] chars in string s to s hashmap
        for i in range(len(p)-1):
            add(s_dict, s[i])
                
        for i in range(len(p)-1, len(s)):   # move slide window to check anagrams
            add(s_dict, s[i])
            if s_dict == p_dict:
                ans.append(i+1-len(p))
            delete(s_dict, s[i+1-len(p)])
        
        return ans