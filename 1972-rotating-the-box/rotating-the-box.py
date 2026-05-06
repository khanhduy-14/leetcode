class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        rows = len(boxGrid)
        cols = len(boxGrid[0])
        rotated_grid = [['' for _ in range(rows)] for _ in range(cols)]



        for i in range(rows):
            stone = 0
            for j in range(cols):
                if boxGrid[i][j] == '#':
                    boxGrid[i][j] = '.'
                    stone+=1

                if (boxGrid[i][j] == '*' or j == cols - 1) and stone > 0:
                    carry = 1 if j == cols - 1 and boxGrid[i][j] == '.' else 0
                    while stone > 0:
                        boxGrid[i][j-stone + carry] = '#'
                        stone-=1

        for i in range(rows):
            for j in range(cols):
                rotated_grid[j][rows - 1 - i] = boxGrid[i][j]


        return rotated_grid



                