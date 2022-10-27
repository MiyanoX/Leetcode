class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:                      # base case
            return nums[0]                      # return the min num
        
        mid = (len(nums) - 1) // 2              # calculate the index of mid item
        if nums[mid] > nums[-1]:                
            return self.findMin(nums[mid+1:])   # the min value is in right part if mid value >> last value
        else:
            return self.findMin(nums[:mid+1])   # otherwise in left part
