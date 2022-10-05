class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        min_heap = []
        
        for i in range(len(mat)):
            min_heap.append([sum(mat[i]), i])
            
        min_heap = heapq.heapify(min_heap)
        res = []
        
        for j in range(k):
            res.append(heapq.heappop(min_heap))
            
        return res

kWeakestRows(0, [[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]],3)        