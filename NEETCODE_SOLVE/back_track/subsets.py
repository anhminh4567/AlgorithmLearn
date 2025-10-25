# https://neetcode.io/problems/subsets?list=neetcode150
# Subsets
# Given an array nums of unique integers, return all possible subsets of nums.

# The solution set must not contain duplicate subsets. You may return the
# solution in any order.

# Example 1:
#
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
from typing import List


class Solution:
    # Time complexity: O(n ∗ 2^n)
    # Space complexity: O(n) extra space.O(2^n)for the output list.
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result: List[List[int]] = []

        def backtrack(cur: int, current_subset: List[int]):
            result.append(current_subset[:])
            for i in range(cur, len(nums)):
                current_subset.append(nums[i])
                backtrack(i + 1, current_subset)
                current_subset.pop()
        backtrack(0, [])
        return result

    # same stuff, but looks clean
    def subsets_DFS(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return res
    # same complexity but much shorter

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            res += [subset + [num] for subset in res]
        return res
