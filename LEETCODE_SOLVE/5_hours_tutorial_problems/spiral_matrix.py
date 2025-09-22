# https://leetcode.com/problems/spiral-matrix/description/

#Given an m x n matrix, return all elements of the matrix in spiral order.

# MEDIUM

from typing import List


class Solution:
    # okk this soltuion is not perfect
    # it qutie complex and unjustable
    # but somehow it beat mother fking 98.42 % :)))))
    def spiralOrder_try(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if len(matrix) < 1:
            return res
        if len(matrix) == 1:
            return matrix[0]
        col_height = len(matrix)
        row_len = len(matrix[0])
        total = col_height * row_len
        left_lim = -1 #0
        right_lim = row_len #row_len -1
        top_lim = 0# 0
        bot_lim = col_height #col_height -1 
        row_idx, col_idx = 0, 0
        row_dir = 1 # 1 = move left, -1 = move right , 0 = no move
        col_dir = 0 # 1 = move down, -1 = move up , 0 = no move 
        while total > 0:
            # val = matrix[col_idx][row_idx]
            # res.append(val)
            if row_dir ==1 and row_idx + 1 == right_lim:
                right_lim -=1
                row_dir = 0
                col_dir = 1
            elif row_dir == -1 and row_idx -1 == left_lim:
                left_lim +=1
                row_dir = 0
                col_dir = -1
            elif col_dir == -1 and col_idx -1 == top_lim:
                top_lim +=1
                row_dir = 1
                col_dir = 0
            elif col_dir == 1 and col_idx + 1 == bot_lim:
                bot_lim -=1
                row_dir = -1
                col_dir = 0
                
            val = matrix[col_idx][row_idx]
            res.append(val)
            row_idx += row_dir
            col_idx += col_dir
            total -=1
        return res
    
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if not matrix or not matrix[0]:
            return res
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        while left <= right and top <= bottom:
            # Traverse from left to right
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            top += 1
            # Traverse downwards
            for row in range(top, bottom + 1):
                res.append(matrix[row][right])
            right -= 1
            if top <= bottom:
                # Traverse from right to left
                for col in range(right, left - 1, -1):
                    res.append(matrix[bottom][col])
                bottom -= 1
            if left <= right:
                # Traverse upwards
                for row in range(bottom, top - 1, -1):
                    res.append(matrix[row][left])
                left += 1
        return res
sol = Solution()
print(sol.spiralOrder_try([[1,2,3],[4,5,6],[7,8,9]]))
print(sol.spiralOrder_try([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))

print(sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(sol.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))

