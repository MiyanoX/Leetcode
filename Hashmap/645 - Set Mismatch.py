class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dict = {}   # hashmap                
        ans = []    # answer list
        sum = 0     # sum of nums
        for num in nums:
            if num in dict:
                ans.append(num)
            else:
                dict[num] = 1
                sum += num
        ans.append(( 1 + len(nums)) * len(nums) // 2 - sum)     # calculate the difference of 1~n sum and nums sum
        return ans