class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        areaList = [0]
        nextGrids = [[0,1], [1,0], [-1,0], [0,-1]]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:  
                    areaList.append(self.bfs(grid, i, j, nextGrids))
        return max(areaList)
    
    def dfs(self, grid, row, col, nextGrids):
        area = 0
        stack = [[row, col]]
        while stack:
            cur = stack.pop()
            area += 1
            grid[cur[0]][cur[1]] = 2

            for nextGrid in nextGrids:
                next = [x + y for x, y in zip(cur, nextGrid)]
                if 0 <= next[0] < len(grid) and 0 <= next[1] <len(grid[0]) and grid[next[0]][next[1]] == 1 and next not in stack:
                    stack.append(next)
        return area
    
    def bfs(self, grid, row, col, nextGrids):
        area = 0
        queue = [[row, col]]
        while queue:
            cur = queue.pop()
            area += 1
            grid[cur[0]][cur[1]] = 2

            for nextGrid in nextGrids:
                next = [x + y for x, y in zip(cur, nextGrid)]
                if 0 <= next[0] < len(grid) and 0 <= next[1] <len(grid[0]) and grid[next[0]][next[1]] == 1 and next not in queue:
                    queue.insert(0, next)
        return area
                