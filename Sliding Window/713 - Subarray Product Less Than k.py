class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        start, end = 0, 0                           # initial sliding window pointers
        ans = 0                                     # count answers
        prod = 1                                    # save product
        
        while end < len(nums):                      
            prod *= nums[end]                       # mutiply next element
            while prod >= k and start <= end:       # if product is bigger then move start pointer
                prod /= nums[start]                 # divide by previous element
                start += 1
            if prod < k:                  
                ans += end - start + 1              # add new count of subarray
            end += 1
        return ans