# https://neetcode.io/problems/two-integer-sum-ii?list=neetcode150
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

#MEDIUM

# Given an array of integers numbers that is sorted in non-decreasing order.
# Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.
# There will always be exactly one valid solution.
# Your solution must use 
# O(1) additional space.

from typing import List


class Solution:
    # solution
    # simple
    #   use a window size 2
    #   while not reaching the end
    #       the sum if < target
    #       => we need a bigger value
    #       => list sorted => move both index 
    #       => why move both ?
    #       =>  this thang ensure the negative num still countable
    #       =>  this also ensure the value will >= target
    #       after that if the sum is now > targe
    #       => we need to use lower numre
    #       => now we move the l -= 1 position
    def twoSum_mySolution(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) < 2:
            return []
        l = 0 
        r = 1
        while r < len(numbers):
            if l >= r:
                return []
            sum = numbers[l] + numbers[r]
            if sum < target:
                r += 1
                l += 1 
                continue
            if sum > target:
                l -= 1
                continue
            return [l +1 ,r + 1] 
        return []

num = [1,2,3,4] 
target = 3
print(Solution().twoSum_mySolution(num,target))
num = [2,7,11,15]
target = 9
print(Solution().twoSum_mySolution(num,target))

num = [2,3,4]
target = 6
print(Solution().twoSum_mySolution(num,target))
num = [-5,-3,0,2,4,6,8]
target = 5 # 2 , 7
print(Solution().twoSum_mySolution(num,target))
