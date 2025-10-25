# https://neetcode.io/problems/generate-parentheses?list=neetcode150
# You are given an integer n. Return all well-formed parentheses strings that you
# generate with n pairs of parentheses.

# Example 1:
# Input: n = 1
# Output: ["()"]

# Example 2:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
from typing import List


class Solution:
    # Time complexity: O(2^(2n) ∗ n)Space complexity: O(2^(2n) ∗ n)
    def generateParenthesis_BRUTEFORCE_DFS(self, n: int) -> List[str]:
        res = []

        def valid(s: str):
            open = 0
            for c in s:
                open += 1 if c == '(' else -1
                if open < 0:
                    return False
            return not open

        def dfs(s: str):
            if n * 2 == len(s):
                if valid(s):
                    res.append(s)
                return

            dfs(s + '(')
            dfs(s + ')')

        dfs("")
        return res
    # using DFS search

    def generateParenthesis_DFS(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res
