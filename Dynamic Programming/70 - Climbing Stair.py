class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        res = [1, 2]
        while len(res) < n:
            res.append(res[-1] + res[-2])
        
        return res[-1]
