class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        ans = []
        
        for i in range(len(grid[0])):
            x, y = i, 0                                                 # set coordinate of start ball
            
            while y < len(grid):                                        # simulate the fall of ball
                if grid[y][x] == 1:                                     # ball to right
                    x += 1
                    if 0 <= x < len(grid[0]) and grid[y][x] == 1:       # check if ball will go down to next row
                        y += 1
                    else:
                        break
                else:                                                   # ball to left
                    x -= 1
                    if 0 <= x < len(grid[0]) and grid[y][x] == -1:      # check if ball will go down to next row
                        y += 1
                    else:
                        break

            if y == len(grid):                                          # check if ball in the bottom
                ans.append(x)
            else:
                ans.append(-1)

        return ans