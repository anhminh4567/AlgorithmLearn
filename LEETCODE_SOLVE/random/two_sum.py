# https://leetcode.com/problems/two-sum/description/
# https://neetcode.io/problems/two-integer-sum?list=neetcode150

# EASY


#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

from typing import List



class Solution:
    # how to solve
    # the list is not ordered => use dictionary<difference, index>()
    # for every num in range
    #   cal the difference ( target - current value) => MAJOR STEP
    #       this is to cal remain value required for the target to succeed
    #       => make this different as key O(1)
    #       => next time check a value if it is a key => we found match at O(1) with n item
    #       => O(N)
    def twoSum_MySolution(self, nums: List[int], target: int) -> List[int]:
        tracker = {}
        for idx in range(len(nums)):
            val = nums[idx]
            difference = target - val
            getVal = tracker.get(val)
            if getVal is None:
                tracker[difference] = idx
            else:
                return [min(idx,getVal),max(idx,getVal)]
        return []
    
    
nums=[-1,-2,-3,-4,-5]
target=-8
print(Solution().twoSum_MySolution(nums,target))