class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        visited = {}                                            # save visited gene in bank
        
        for gene in bank:                                       
            visited[gene] = False
            
        queue = [(start, 0)]                                    # record mutation gene and number of mutation
        while queue:
            cur, level = queue.pop(0)                           # pop out first item in queue
            if cur == end:                                      # if reach end gene, return mutation level
                return level
            
            for i in range(len(cur)):                           # find next possible mutation gene
                for char in 'ACGT':
                    if char == cur[i]:
                        continue
                    next = cur[:i] + char + cur[i+1:]
                    if next in visited and not visited[next]:
                        queue.append((next, level+1))
                        visited[next] = True
        return -1                                               # if no possible mutation, return -1 