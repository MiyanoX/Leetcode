class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        def intersect(l1, l2):                                  # help function to calculate intersection area of two list
            start = max(l1[0], l2[0])
            end = min(l1[1], l2[1])
            if start <= end:
                return [[start, end]]
            else:
                return []                                       # if no intersection, return empty list
        
        p1, p2 = 0, 0                                           # set two pointers
        ans = []
        while p1 < len(firstList) and p2 < len(secondList):
            ans += intersect(firstList[p1], secondList[p2])     # add intersection result to answer list
            if firstList[p1][1] < secondList[p2][1]:
                p1 += 1                                         # if end of p1 list is smaller, p1 += 1 
            else:
                p2 += 1                                         # else, p2 += 1
        return ans