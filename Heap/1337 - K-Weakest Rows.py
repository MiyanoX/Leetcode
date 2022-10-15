class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        min_heap = []
        
        for i in range(len(mat)):
            min_heap.append([sum(mat[i]), i])
            
        heapq.heapify(min_heap)
        res = []

        for j in range(k):
            res.append(heapq.heappop(min_heap)[1])
            
        return res