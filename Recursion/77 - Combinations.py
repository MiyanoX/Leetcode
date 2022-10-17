class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 1:
            return [[i] for i in range(1, n+1)]
        
        res = self.combine(n-1, k-1) 
        for lst in res:
            lst.append(n)
            
        if n - 1 >= k:
            res += self.combine(n-1, k)
            
        return res