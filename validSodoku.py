class Solution: 
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # Check Rows
        seen = set()
        for row in board:
            seen.clear()
            for cell in row:
                if cell == ".": continue
                if cell in seen: return False
                seen.add(cell)
                
        # Check Columns
        for col in range(9):
            seen.clear()
            for row in board:
                cell = row[col]
                if cell == ".": continue
                if cell in seen: return False
                seen.add(cell)
                
        # Check Boxes
        for i in range(3):
            for j in range(3):
                seen.clear()
                for di in range(3):
                    for dj in range(3):
                        cell = board[3*i+di][3*j+dj]
                        if cell == ".": continue
                        if cell in seen: return False
                        seen.add(cell)
                    
        return True
    
    
        # Cleaner 1 Pass Solution (https://leetcode.com/problems/valid-sudoku/solution/)
        
        #         N = 9

        #         # Use hash set to record the status
        #         rows = [set() for _ in range(N)]
        #         cols = [set() for _ in range(N)]
        #         boxes = [set() for _ in range(N)]

        #         for r in range(N):
        #             for c in range(N):
        #                 val = board[r][c]
        #                 # Check if the position is filled with number
        #                 if val == ".":
        #                     continue

        #                 # Check the row
        #                 if val in rows[r]:
        #                     return False
        #                 rows[r].add(val)

        #                 # Check the column
        #                 if val in cols[c]:
        #                     return False
        #                 cols[c].add(val)

        #                 # Check the box
        #                 idx = (r // 3) * 3 + c // 3
        #                 if val in boxes[idx]:
        #                     return False
        #                 boxes[idx].add(val)

        #         return True