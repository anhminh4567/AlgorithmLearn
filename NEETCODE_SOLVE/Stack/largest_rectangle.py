
# https://neetcode.io/problems/largest-rectangle-in-histogram


# You are given an array of integers heights where heights[i] represents
# the height of a bar. The width of each bar is 1.
# # Return the area of the largest rectangle that can be formed among the bars.
# You should aim for a solution with O(n) time and O(n) space, where n is the size of the input array.
from operator import le


heights1 = [7, 1, 7, 2, 2, 4]  # 8
heights2 = [1, 3, 7]  # 7


class Solution:
    # Time Complexity: O(n) (linear, as we traverse the array once).
    # Space Complexity: O(n) (linear, as we use a stack to store indices).
    def largestRectangleArea_optimal(self, heights: list[int]) -> int:
        maxArea = 0
        stack = []  # pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea
    # Time Complexity: O(n) (linear, as we traverse the array once).
    # Space Complexity: O(n) (linear, as we use a stack to store indices).
    # this method is identitcal to the trapping rain water problem

    def largestRectangleArea_suggested(self, heights: list[int]) -> int:
        n = len(heights)
        stack = []
        leftMost = [-1] * n
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                leftMost[i] = stack[-1]
            stack.append(i)

        stack = []
        rightMost = [n] * n
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                rightMost[i] = stack[-1]
            stack.append(i)

        maxArea = 0
        for i in range(n):
            leftMost[i] += 1
            rightMost[i] -= 1
            maxArea = max(maxArea, heights[i] *
                          (rightMost[i] - leftMost[i] + 1))
        return maxArea
        # calculate the ared for each bar
        # Time Complexity: O(n²) (quadratic due to the nested loops).
        # Space Complexity: O(1) (constant, as no extra space is used).

    def largestRectangleArea_Brute(self, heights: list[int]) -> int:
        max_area = 0
        if not heights:
            return max_area
        if len(heights) == 1:
            return heights[0]
        # start shit here
        max_area = heights[0]
        for i in range(len(heights)):
            if heights[i] > max_area:
                max_area = heights[i]
            min_height = heights[i]
            for j in range(i + 1, len(heights)):
                width = j - i + 1
                height = min(heights[j], min_height)
                min_height = height
                area = width * height
                if area > max_area:
                    max_area = area
        return max_area


sol = Solution()
# print(sol.largestRectangleArea_Brute(heights1))
# print(sol.largestRectangleArea_Brute(heights2))

print(sol.largestRectangleArea_suggested(heights1))
print(sol.largestRectangleArea_suggested(heights2))
