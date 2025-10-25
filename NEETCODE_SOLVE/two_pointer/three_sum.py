# https://neetcode.io/problems/three-integer-sum?list=neetcode150
# RECOMMENDATION: solve 2 sum + 2 sum II => this will be easy
# MEDIUM

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

# The output should not contain any duplicate triplets. You may return the output and the
# triplets in any order

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

# Example 2:
# Input: nums = [0,1,1]
# Output: []

# Example 3:
# Input: nums = [0,0,0]
# Output: [[0,0,0]]

# You should aim for a solution with O(n^2) time and O(1) space, where n is the size of the input array.
from typing import List


class Solution:
    # O(n^3) for speed and who the hell know how much space this take
    def threeSum_terrible(self, nums: List[int]) -> List[List[int]]:
        track = set()
        result = []
        for i in range(0, len(nums)):
            sub_res = []
            j = i + 1
            while j < len(nums):
                k = j + 1
                while k < len(nums):
                    if nums[k] + nums[j] + nums[i] == 0:
                        sub_res = [nums[k], nums[j], nums[i]]
                        sub_res.sort()
                        as_str = f"{str(sub_res[0])}{str(sub_res[1])}{str(sub_res[2])}"
                        if as_str in track:
                            k += 1
                            continue
                        track.add(as_str)
                        result.append(sub_res.copy())
                    k += 1
                j += 1
        return result

    # Time complexity: O(n 3)
    # Space complexity: O(m) m is number of triplet
    # this brute greate spot is SORT() before doing iteration
    # also TUPLE(array ) exist !!
    def threeSum_BRUTE(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        tmp = [nums[i], nums[j], nums[k]]
                        res.add(tuple(tmp))
        return [list(i) for i in res]


nums = [-1, 0, 1, 2, -1, -4]  # Output: [[-1,-1,2],[-1,0,1]]
print(Solution().threeSum_terrible(nums))
