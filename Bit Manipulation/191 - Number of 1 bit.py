class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            n = n & n-1 # delete the first 1 from right side in n
            ans += 1
        return ans
        
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            ans += n & 1 # plus the right digit to answer
            n >>= 1  # move one digit to right
        return ans