class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = -1 # target row

        # first search for row
        fr, lr = 0, len(matrix)-1
        while fr <= lr:
            mr = (fr+lr)//2
            if matrix[mr][0] <= target <= matrix[mr][-1]:
                row = mr
                break
            elif matrix[mr][0] > target:
                lr = mr - 1
            else:
                fr = mr + 1
        
        # return False if no availble row
        if row == -1:
            return False
        
        # second search for column
        fl, ll = 0, len(matrix[row])-1
        while fl <= ll:
            ml = (fl+ll)//2
            if matrix[row][ml] == target:
                return True
            elif matrix[row][ml] > target:
                ll = ml - 1
            else:
                fl = ml + 1

        # return False if no availble column
        return False