class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()                                                 # sort list 
        ans = []
        for i in range(len(nums)-2):
            f, l = i+1, len(nums)-1                                 # set two pointers 
            while f < l:
                if nums[i] + nums[f] + nums[l] == 0:                # if sum == 0
                    lst = [nums[i], nums[f], nums[l]]
                    if lst not in ans:                              # if sum not in ans list
                        ans.append([nums[i], nums[f], nums[l]])     # add three index to ans list
                    f += 1                                          
                    l -= 1
                elif nums[i] + nums[f] + nums[l] < 0:               # if sum < 0, increase the first pointer
                    f += 1
                else:                                               # if sum > 0, decrease the last pointer
                    l -= 1
        return ans