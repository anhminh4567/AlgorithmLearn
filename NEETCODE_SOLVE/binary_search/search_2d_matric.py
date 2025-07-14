# https://neetcode.io/problems/search-2d-matrix?list=neetcode150
# Search a 2D Matrix
# You are given an m x n 2-D integer array matrix and an integer target.
# MEDIUM
# Each row in matrix is sorted in non-decreasing order.
# The first integer of every row is greater than the last integer of the previous row.
# Return true if target exists within matrix or false otherwise.

# Can you write a solution that runs in O(log(m * n)) time?
# Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10

# Output: true
from typing import List
# Output: true
from typing import List

# we did reach o(log(m*n) == log m + log n with m being matrix row, n being row length)
# BUT our space complexity is o(1), BUT :))) we can replace all those temp value with direct
# calculation on the spot, we basically allocate no space :))) some devious stuff
class Solution_yourown:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        return self.many_row_filter(matrix,target,0, len(matrix))
    def many_row_filter(self, matrix: List[List[int]], target: int, start: int, end: int) -> bool:
        if start > end:
            return False        
        mid = (start + end) // 2
        if mid >= len(matrix):
            return False
        mid_arr = matrix[mid]
        
        if mid_arr[0] <= target and mid_arr[-1] >= target:
            return self.row_search(mid_arr,target,0 ,len(mid_arr) -1)
        elif mid_arr[-1] < target:
            return self.many_row_filter(matrix,target, mid + 1,end)
        else:
            return self.many_row_filter(matrix,target,start,mid - 1) 
        
    def row_search(self, row: List[int], target: int, start: int, end: int):
        if start > end:
            return False
        mid = (start + end) // 2
        if mid >= len(row):
            return False
        mid_val = row[mid]
        if mid_val == target:
            return True
        if mid_val < target:
            return self.row_search(row, target, mid + 1, end )
        else:
            return self.row_search(row,target, start, mid - 1)

# Time complexity: O(m+n)
# Space complexity: O(1)
# this solution is quite interesting
# go from last column, check and move accordingly to startcase
class Solution_staircase:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        r, c = 0, n - 1

        while r < m and c >= 0:
            if matrix[r][c] > target:
                c -= 1
            elif matrix[r][c] < target:
                r += 1
            else:
                return True
        return False
    
#  Time complexity: O(log⁡m+log⁡n)
#  (which reduces to O(log⁡(m∗n)))
#  Space complexity: O(1)
# same as our but more stack efficient 
class Solution_standard:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        if not (top <= bot):
            return False
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False