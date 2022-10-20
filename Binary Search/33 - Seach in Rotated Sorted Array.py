class Solution:
    def search(self, nums: List[int], target: int) -> int:
		# set start and end
        start, end = 0, len(nums) - 1
		
		# if list is rotated, apply first binary search to find mid point
        if nums[0] > nums[-1]:
            while start <= end:
                i = (start + end) // 2
                if nums[i] > nums[i+1]:
                    if target >= nums[0]:
                        start, end = 0, i
                    else:
                        start, end = i+1, len(nums) - 1
                    break
                elif nums[i] >= nums[0]:
                    start = i + 1
                else:
                    end = i - 1
		
		# according to the previous result, use the second binary search to find target
        while start <= end:
            i = (start + end) // 2        
            if nums[i] == target:
                return i
            elif nums[i] < target:
                start = i + 1
            else:
                end = i - 1
        
		# if target not in list return -1
        return -1