# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        # set start and end pointers
        start, end = 1, n
        
        # binary search
        while start <= end:
            mid = (start + end) // 2
            if isBadVersion(mid):
                if mid == 1 or not isBadVersion(mid-1): # consider about case result is 1 & find the first bad version
                    return mid
                end = mid - 1
            else:
                start = mid + 1