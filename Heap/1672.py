class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        # create a max heap list
        max_heap = []
        
        # append sum of row into row
        for customer in accounts:
            max_heap.append(-1 * sum(customer)) # use -1 to reverse heapq
            
        # heapify
        heapq.heapify(max_heap)
        
        return -1 * heapq.heappop(max_heap) # use -1 to return right value