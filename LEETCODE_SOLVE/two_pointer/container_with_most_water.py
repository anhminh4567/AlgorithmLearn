# https://neetcode.io/problems/max-water-container
import math

height = [1, 7, 2, 5, 4, 7, 3, 6]
height2 = [2, 2, 2]


class Solution:
    def maxArea(self, heights: list[int]) -> int:
        max = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            width = right - left
            minHeight = min(heights[left], heights[right])
            smaller = min(heights[left], heights[right])
            area = minHeight * width
            if area > max:
                max = area
            if smaller == heights[left]:
                left += 1
            else:
                right -= 1
        return max


sol = Solution()
print(sol.maxArea(height))  # 49
print(sol.maxArea(height2))  # 4
