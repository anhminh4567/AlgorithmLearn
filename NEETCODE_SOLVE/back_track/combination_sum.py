# https://neetcode.io/problems/combination-target-sum?list=neetcode150
# You are given an array of distinct integers nums and a target integer target.
# Your task is to return a list of all unique combinations of nums where the
# chosen numbers sum to target.

# The same number may be chosen from nums an unlimited number of times. Two
# combinations are the same if the frequency of each of the chosen numbers is
# the same, otherwise they are different.

# You may return the combinations in any order and the order of the numbers in
# each combination can be in any order.
# Input:
# nums = [2,5,6,9]
# target = 9
# Output: [[2,2,5],[9]]
# You should aim for a solution with O(2^(t/m)) time and O(t/m) space,
# where t is the given target and m is the minimum value in the given array.


from typing import List
# idea, loop at one position until the value > target then return
# go next, else if == ADD to result, else < then continue at that pos


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        subset = []
        result = []

        def dfs(i: int, current: int):
            if current > target or i >= len(nums):
                return
            if current == target:
                result.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i, current + nums[i])
            subset.pop()
            dfs(i + 1, current)
        dfs(0, 0)
        return result


nums = [2, 5, 6, 9]
target = 9
# Output: [[2,2,5],[9]]
print(Solution().combinationSum(nums, target))
