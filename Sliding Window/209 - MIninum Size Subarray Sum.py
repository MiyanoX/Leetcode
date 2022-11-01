class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start, end = 0, 0                                           # initial window
        min_length = float('inf')                                   # save min of window length
        nums_sum = 0                                                # save sum in the window
        
        while end < len(nums):
            nums_sum += nums[end]                                   # add end element to sum
            end += 1                                                # move end pointer
            while nums_sum >= target:                               # if sum > target, move start point until sum < target
                min_length = min(min_length, end - start)           # update min
                nums_sum -= nums[start]                             # delete start element from sum
                start += 1                                          # move start pointer
                
        return 0 if min_length == float('inf') else min_length      # if min_length not updated, return 0