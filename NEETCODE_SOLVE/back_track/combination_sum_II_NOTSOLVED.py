# https://neetcode.io/problems/combination-target-sum-ii?list=neetcode150
# COMBINATION SUM II
# MEDIUM ( WE DID NOT SOLVE THIS)
# go watch how to solve
'''
You are given an array of integers candidates, which may contain duplicates, 
and a target integer target. Your task is to return a list of all unique combinations 
of candidates where the chosen numbers sum to target.

Each element from candidates may be chosen at most once within a combination. 
The solution set must not contain duplicate combinations.

You may return the combinations in any order and the order of the numbers 
in each combination can be in any order.

Example 1:
Input: candidates = [9,2,2,4,6,1,5], target = 8
Output: [
  [1,2,5],
  [2,2,4],
  [2,6]
]
Example 2:
Input: candidates = [1,2,3,4,5], target = 7
Output: [
  [1,2,4],
  [2,5],
  [3,4]
]
'''
from typing import List


class Solution:
    # NOT WORKING
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = set()
        # cur_indx: int
        candidates.sort()

        def dfs(idx: int, stack: List[int], cur_sum: int):
            if (idx >= len(candidates) or cur_sum > target):
                return
            if cur_sum == target:
                copied = stack.copy()
                result.add(tuple(copied))
                return
            stack.append(candidates[idx])
            dfs(idx + 1, stack, cur_sum + candidates[idx])
            stack.pop()
            # it can only be solved by adding this line
            # but why ? WE DO NOT KNOW !!!!!
            # THIS IS MAJOR, all backtrack do thi
            dfs(idx + 1, stack, cur_sum)
        dfs(0, [], 0)

        return [list(i) for i in result]

    def combinationSum2_CORRECT(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if total > target or i == len(candidates):
                return

            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])
            cur.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res


candidates = [9, 2, 2, 4, 6, 1, 5]
target = 8
print(Solution().combinationSum2(candidates, target))
print(Solution().combinationSum2_CORRECT(candidates, target))

# candidates = [1, 2, 3, 4, 5]
# target = 7
# print(Solution().combinationSum2(candidates, target))
