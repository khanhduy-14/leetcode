class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row, col = len(matrix), len(matrix[0])
        x,y,dx,dy = 0,0,0,1
        result = []
        for _ in range(row * col):
            result.append(matrix[x][y])
            matrix[x][y] = '.'

            if not 0 <= x + dx <= row - 1 or not 0 <= y + dy <= col - 1 or matrix[x+dx][y+dy] == '.':
                dx,dy=dy,-dx
            
            x+=dx
            y+=dy
        
        return result
        