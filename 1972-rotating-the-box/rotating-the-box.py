class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        rows, cols = len(boxGrid), len(boxGrid[0])

        for i in range(rows):
            write = cols - 1
            for j in range(cols - 1, -1, -1):
                if boxGrid[i][j] == '*':
                    write = j - 1
                elif boxGrid[i][j] == '#':
                    boxGrid[i][j] = '.'
                    boxGrid[i][write] = '#'
                    write -= 1

        rotated = [[None] * rows for _ in range(cols)]
        for i in range(rows):
            for j in range(cols):
                rotated[j][rows - 1 - i] = boxGrid[i][j]

        return rotated