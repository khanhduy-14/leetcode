class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])

        idx = 0

        def findAround(r: int, c: int, idx: int):
            if r < 0 or r > row - 1 or c < 0 or c > col - 1:
                return False

            letter = board[r][c]
            if word[idx] == letter and letter != '.':
                if idx >= len(word) - 1:
                    return True
                else:
                    idx += 1
                    board[r][c] = '.'

                    if findAround(r+1, c, idx) or findAround(r-1, c, idx):
                        return True
                    if findAround(r, c + 1, idx) or findAround(r, c - 1, idx):
                        return True
                    
                    idx-=1
                    board[r][c] = letter
                    return False
            else:
                return False
            

        for r in range(row):
            for c in range(col):
                if findAround(r,c, idx):
                    return True
        
        return False

                    




        