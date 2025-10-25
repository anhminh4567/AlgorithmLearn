# https://neetcode.io/problems/longest-consecutive-sequence?list=neetcode150
# MEDIUM

# Longest Consecutive Sequence
# Given an array of integers nums, return the length of the longest consecutive sequence
# of elements that can be formed.

# A consecutive sequence is a sequence of elements in which each element is exactly 1
# greater than the previous element. The elements do not have to be consecutive in the original array.

# You must write an algorithm that runs in O(n) time.

# Example 1:
# Input: nums = [2,20,4,10,3,4,5]
# Output: 4 | Explanation: The longest consecutive sequence is [2, 3, 4, 5].
# Example 2:
# Input: nums = [0,3,2,5,4,6,1,1]
# Output: 7
from collections import defaultdict
from typing import List


class Solution:
    # O(n log n ) get idea from result
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        i = 1
        streak = 1
        res = streak
        while i < len(nums):
            curr = nums[i]
            prev = nums[i - 1]
            if curr == prev:
                i += 1
            if prev == (curr - 1):
                streak += 1
                i += 1
            if prev < (curr - 1):
                streak = 1
                i += 1
            res = max(res, streak)
        return res
    # O(n) most optimized

    def longestConsecutive_best(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest


nums = [2, 20, 4, 10, 3, 4, 5]
print(Solution().longestConsecutive(nums))
nums = [0, 3, 2, 5, 4, 6, 1, 1]
print(Solution().longestConsecutive(nums))
nums = [0]
print(Solution().longestConsecutive(nums))
