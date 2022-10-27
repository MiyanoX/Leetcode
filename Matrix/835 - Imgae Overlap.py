class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        l = len(img1)                   # side length of matrix
        
        p1, p2 = [], []                 # 1-point list of img1 and img2
        for r in range(l):
            for c in range(l):
                if img1[r][c] == 1:
                    p1.append((r,c))
                if img2[r][c] == 1:
                    p2.append((r,c))
        
        d = {None: 0}                   # create dictionary to count vectors of p1 -> p2 (initial dictionary with 0 case)
        for r1, c1 in p1:
            for r2, c2 in p2:
                v = (r1-r2, c1-c2)      # calculte the vector from p1 to p2
                if v not in d:
                    d[v] = 1
                else:
                    d[v] += 1
        return max(d.values())          # return the vector with max count