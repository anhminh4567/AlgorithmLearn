# https://neetcode.io/problems/max-area-of-island?list=neetcode250
# medium
'''
You are given a matrix grid where grid[i] is either a 0 (representing water) 
or 1 (representing land).

An island is defined as a group of 1's connected horizontally or vertically.
You may assume all four edges of the grid are surrounded by water.

The area of an island is defined as the number of cells within the island.

Return the maximum area of an island in grid. If no island exists, return 0.
'''


from collections import deque
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # [row, col]
        # [right, left, up, down]
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        max_area = 0

        def isInValid(r, c):
            return r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0

        def bfs(r: int, c: int):
            area = 1
            q = deque()
            q.append((r, c))
            grid[r][c] = 0
            while q:
                row, col = q.popleft()
                for drow, dcol in directions:
                    nrow, ncol = row+drow, col + dcol
                    if isInValid(nrow, ncol):
                        continue
                    grid[nrow][ncol] = 0
                    area += 1
                    q.append((nrow, ncol))
            return area

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    continue
                max_area = max(max_area, bfs(row, col))
        return max_area
