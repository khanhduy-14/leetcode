class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        res,queen_positions =[], []
        def check_valid_queen_position(r, c):
            for [cr, cc] in queen_positions:
                if cr == r or cc == c or abs(cr-r) == abs(cc-c):
                    return False
            
            return True
        if n == 1:
            return [['Q']]
        def backtrack(i, curr):
            if i >= n:
                res.append(curr.copy())
                return
            for j in range(n):
                if check_valid_queen_position(i, j):
                    row = ['.'] * n  
                    row[j] = 'Q'    
                    row = ''.join(row)
                    queen_positions.append([i,j])
                    curr.append(row)
                    backtrack(i+1, curr)
                    queen_positions.pop()
                    curr.pop()

        backtrack(0, [])

        return res