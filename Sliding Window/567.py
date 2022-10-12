class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_dict = {}
        for char in s1:
            self.dict_insert(s1_dict, char)
            
        start, end = 0, len(s1)-1
        s2_dict = {}
        
        for i in range(start, end):
            self.dict_insert(s2_dict, s2[i])
            
        while end < len(s2):
            self.dict_insert(s2_dict, s2[end])
            
            if s1_dict == s2_dict:
                return True
            else:
                self.dict_delete(s2_dict, s2[start])
                start, end = start + 1, end + 1
                
        return False
                
            
    def dict_insert(self, d:dict, char:str):
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1
            
    def dict_delete(self, d:dict, char:str):
        if d[char] > 1:
            d[char] -= 1
        else:
            del d[char]