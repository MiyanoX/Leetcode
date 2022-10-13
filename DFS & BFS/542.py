class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        Row, Col = len(mat), len(mat[0])
        # queue of 0s
        queue = []
        visited = set()
        directions = [(0,1), (0,-1), (1, 0), (-1, 0)]
        for row in range(Row):
            for col in range(Col):
                if mat[row][col]==0:
                    queue.append((row,col))
                    visited.add((row,col))
                else:
                    mat[row][col]= -1
        for row, col in queue:
            for x, y in directions:
                rx, cy = row + x, col + y
                
                if 0 <= rx < Row and 0 <= cy < Col and mat[rx][cy]==-1:
                    mat[rx][cy]=mat[row][col]+1
                    queue.append((rx, cy))
        return mat