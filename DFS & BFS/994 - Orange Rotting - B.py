class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minute, count = 0, 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        queue = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append([i, j])
                if grid[i][j] == 1:
                    count += 1

        while queue:
            length = len(queue)
            for _ in range(length):
                cur = queue.pop(0)
                for direction in directions:
                    new = [cur[0] + direction[0], cur[1] + direction[1]]
                    if 0 <= new[0] < len(grid) and 0 <= new[1] < len(grid[0]) and grid[new[0]][new[1]] == 1:
                        grid[new[0]][new[1]] = 2
                        count -= 1
                        queue.append(new)
            if len(queue) > 0:
                minute += 1

        if count == 0:
            return minute
        else:
            return -1