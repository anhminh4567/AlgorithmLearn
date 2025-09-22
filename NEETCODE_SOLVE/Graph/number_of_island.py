# https://neetcode.io/problems/count-number-of-islands?list=neetcode250
# MEDIUM

# Given a 2D grid grid where '1' represents land and '0' represents water, count and
# return the number of islands.

# An island is formed by connecting adjacent lands horizontally or vertically and
# is surrounded by water. You may assume water is surrounding the grid
# (i.e., all the edges are water).


from collections import deque
from typing import List


class Solution:
    '''
    Note this shit, List[List[str]] => means position(y,x)
    y is row
    x is column 
    mf we make this mistake for dozens of times :))
    note this, we are used to x,y being norm
    OR AT LEASTE NOTE IT OUT
    in this case, we keep (x,y) but the tracker and grid, careful
    '''

    def numIslands_ourSolution_DFS(self, grid: List[List[str]]) -> int:
        height_lim = len(grid) - 1
        width_lim = len(grid[0]) - 1

        # tracker
        tracker: List[List[bool]] = [[False for _ in range(
            0, len(grid[0]))] for _ in range(0, len(grid))]

        def isOffLimit(pos: tuple[int, int]):
            pos_x = pos[0]
            pos_y = pos[1]
            if pos_x < 0 or pos_x > width_lim:
                return True
            if pos_y < 0 or pos_y > height_lim:
                return True
            return False

        def isWater(pos: tuple[int, int]):
            pos_x = pos[0]
            pos_y = pos[1]
            if grid[pos_y][pos_x] == "0":
                return True
            return False

        def isVisited(pos: tuple[int, int]):
            pos_x = pos[0]
            pos_y = pos[1]
            return tracker[pos_y][pos_x]

        def dfs(cur: tuple[int, int]):
            if isOffLimit(cur):
                return
            if isWater(cur):
                return
            if isVisited(cur):
                return
            cur_x = cur[0]
            cur_y = cur[1]
            bot, top, left, right = cur_y, cur_y, cur_x, cur_x

            # note this shit, y is before x, because of the matrix
            tracker[cur_y][cur_x] = True
            if cur_y > 0:
                top = cur_y - 1
            if cur_y < height_lim:
                bot = cur_y + 1
            if cur_x > 0:
                left = cur_x - 1
            if cur_x < width_lim:
                right = cur_x + 1
            dfs((cur_x, top))
            dfs((cur_x, bot))
            dfs((left, cur_y))
            dfs((right, cur_y))
            return

        islandCount = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                current_node = (x, y)
                if isWater((x, y)) or isVisited((x, y)):
                    continue
                dfs(current_node)
                islandCount += 1

        return islandCount
    '''
    this is from the answer part
    '''

    def numIslands_GIVEN_DFS(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or
                    c >= COLS or grid[r][c] == "0"
                    ):
                return

            grid[r][c] = "0"
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1

        return islands
    '''
    from the answer, BFS method, similar to DFS, 
    '''

    def numIslands_GIVEN_BFS(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def bfs(r, c):
            q = deque()
            grid[r][c] = "0"
            q.append((r, c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if (nr < 0 or nc < 0 or nr >= ROWS or
                                nc >= COLS or grid[nr][nc] == "0"
                            ):
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = "0"

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1

        return islands


case = [
    ["0", "1", "1", "1", "0"],
    ["0", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
print(Solution().numIslands_ourSolution_DFS(case))
case = [
    ["1", "1", "0", "0", "1"],
    ["1", "1", "0", "0", "1"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
print(Solution().numIslands_ourSolution_DFS(case))


# we come to a cursed solution, but it is a solution after all using a unique method
# DISJOINT UNION SET

class DSU:
    def __init__(self, n):
        self.Parent = list(range(n + 1))
        self.Size = [1] * (n + 1)

    def find(self, node):
        if self.Parent[node] != node:
            self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        if self.Size[pu] >= self.Size[pv]:
            self.Size[pu] += self.Size[pv]
            self.Parent[pv] = pu
        else:
            self.Size[pv] += self.Size[pu]
            self.Parent[pu] = pv
        return True


class SolutionWEIRD:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dsu = DSU(ROWS * COLS)

        def index(r, c):
            return r * COLS + c

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        islands = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    islands += 1
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if (nr < 0 or nc < 0 or nr >= ROWS or
                            nc >= COLS or grid[nr][nc] == "0"
                            ):
                            continue

                        if dsu.union(index(r, c), index(nr, nc)):
                            islands -= 1

        return islands
