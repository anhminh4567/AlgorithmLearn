# https://neetcode.io/problems/trapping-rain-water
# Trapping Rain Water
# You are given an array non-negative integers height which represent an
# elevation map. Each value height[i] represents the height of a bar,
# which has a width of 1.Return the maximum area of water that
# can be trapped between the bars.

# Example 1
# HARD
# ??????????? unsolved
# this is a veery good problem to solve
# so the formulat to count thee water volume at a given index i is:
# water[i] = min(max_left[i], max_right[i]) - height[i]
# SO:
# min (max left, max right )
# ====> at a given index, we detect like wheere doees this index
# is placed between the bucket ( max left and max right)
# ====> so in that bucket, at that index, we minus the height of index
# ====> now we have the volume of water we need
import math


height = [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]  # 9
height2 = [0, 0, 0, 0]
height3 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]  # 6


class Solution:
    # brute force solution O(n^2) with O(1) space complexity
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0
        n = len(height)
        res = 0
        for i in range(n):
            leftMax = rightMax = height[i]
            for j in range(i):
                leftMax = max(leftMax, height[j])
            for j in range(i + 1, n):
                rightMax = max(rightMax, height[j])
            res += min(leftMax, rightMax) - height[i]
        return res
    # this is a better solution with O(n) time complexity and O(n) space complexity
    # but the thing is , 3 loop, so basically 3n ( but we only cound O(n) )

    def trap2(self, height: list[int]) -> int:
        '''
        this method is basically, we go to each index, and said, at this 
        index, max on left is this and put in an array, and max on right 
        is this and also put in array, then we work purely on the array to 
        cal the volume
        '''
        if not height:
            return 0
        n = len(height)
        leftMax = [0] * n
        rightMax = [0] * n
        res = 0
        leftMax[0] = height[0]
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])
        rightMax[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])
        for i in range(n):
            res += min(leftMax[i], rightMax[i]) - height[i]
        return res
    # O(n) time complexity and O(n) space complexity
    # n for the stack size

    def trap3(self, height: list[int]) -> int:
        '''
        this also a brilliant solution, using a stack, this we thought of before
        but we fail to implement it, basically
        one man walk, each walk, check if ( stack==step we move without stop from last stop )
        ( and the height of the curreent step is greater or equal the previous step)
        ===> if that the case, we pop() step ( == check till we find the last
        stop, means we have a bucket) ===> then we move on, take the current position as the new 
        stop, and move 
        '''
        if not height:
            return 0
        stack = []
        res = 0
        for i in range(len(height)):
            while stack and height[i] >= height[stack[-1]]:
                mid = height[stack.pop()]
                if stack:
                    right = height[i]
                    left = height[stack[-1]]
                    h = min(right, left) - mid
                    w = i - stack[-1] - 1
                    res += h * w
            stack.append(i)
        return res
    # O(n) time complexity and O(1) space complexity

    def trap_2_pointer_best_solution(self, height: list[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res


sol = Solution()
print(sol.trap(height))  # 10
print(sol.trap(height2))  # 10
print(sol.trap(height3))  # 6
