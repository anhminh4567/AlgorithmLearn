# https://neetcode.io/problems/valid-sudoku


class Solution:
    _empty = "."
    def isValidSudoku(self, board: list [list[str]]) -> bool:
        row_set = set()
        column_set = set()
        # checkrow
        for i,row in enumerate(board):
            for idx,cell in enumerate(row):
                if cell == self._empty:
                    continue
                
                pair: tuple[int, str] = (i , cell)
                if pair in row_set:
                    return False
                row_set.add(pair)
                
        # check col
        for i in range(0,9):
            col_index = i
            for  idx,row in enumerate(board):
                val = row[col_index]
                if val == self._empty:
                    continue
                
                pair = (col_index,val)
                if pair in column_set:
                    return False
                column_set.add(pair)
        
        # check square, this thang will go top to bot, left to right
   
        for row in range(0,3):
            for col in range(0,3):
                square_set = set()
                # each time we do 9 times
                # equal the sq in big sq
                x = row * 3
                y = col * 3
                max_X = x + 3
                max_y = y + 3
                print(f"x: {x}; y: {y}, maxX: {max_X}; maxY: {max_y}")
                while x < max_X:
                    default_y = y
                    while y < max_y:
                        val: str = board[x][y]
                        if val != self._empty:
                            if val in square_set:
                                return False
                            else:
                                square_set.add(val)
                        y +=1
                    y = default_y
                    x += 1
        return True                
                
        
        
        



board_1: list[list[str]] = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

result = Solution().isValidSudoku(board_1)
print(result)

