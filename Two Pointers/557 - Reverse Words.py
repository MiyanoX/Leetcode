class Solution:
    def reverseWords(self, s: str) -> str:
        p1, p2 = 0, 0
        res = ""
        
        while p2 <= len(s):
            
            if p2 == len(s) or s[p2] == " ":
                for i in range(p2-1, p1-1, -1):
                    res += s[i]
                
                if p2 != len(s):
                    res += " "             
                p2 += 1
                p1 = p2
            
            else:
                p2 += 1
                
        return res