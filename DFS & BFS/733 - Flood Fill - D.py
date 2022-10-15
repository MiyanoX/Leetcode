class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start_color = image[sr][sc]
        stack = [[sr, sc]]
        while stack:
            row, col = stack.pop()
            if image[row][col] != start_color or image[row][col] == color:
                continue
                
            image[row][col] = color
            next = self.nextPixel(image, row, col)
            stack += next
        return image   
        
        
    def nextPixel(self, image, cr:int, cc:int):
        res = []
        if cr - 1 >= 0:
            res.append([cr-1, cc])
        if cr + 1 < len(image):
            res.append([cr+1, cc])
        if cc - 1 >= 0:
            res.append([cr, cc-1])
        if cc + 1 < len(image[0]):
            res.append([cr, cc+1])
        return res