class Solution:
    def maxArea(self, height: List[int]) -> int:
        start, end = 0, len(height) - 1                     # set two pointers
        area = 0
        
        while start < end:
            min_height = min(height[start], height[end])    # calculate the lower sides
            area = max(area, min_height * (end - start))    # calculate water volume and update max volume
            if height[start] < height[end]:                 # judge which pointer need to be moved
                start += 1 
                while height[start] < min_height:           # move pointer until the side is higher than previous lower side
                    start += 1
            else:
                end -= 1
                while height[end] < min_height:
                    end -= 1
        return area
    