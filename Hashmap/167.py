class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict = {}
        
        for i in range(len(numbers)):
            if numbers[i] not in dict:
                dict[target - numbers[i]] = i + 1
            else:
                return [dict[numbers[i]], i + 1]