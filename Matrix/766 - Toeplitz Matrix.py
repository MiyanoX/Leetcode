class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(1-len(matrix[0]), len(matrix)):
            x, y = i, 0
            num = None
            
            while x < len(matrix) and y < len(matrix[0]):
                if x >= 0:
                    if num is None:
                        num = matrix[x][y]
                    elif matrix[x][y] != num:
                        return False
                x += 1
                y += 1
                
        return True
                