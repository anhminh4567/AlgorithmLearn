# https://neetcode.io/problems/validate-parentheses
# this is how static code analizyeer logic work 
class Solution:

    def isValid(self, s: str) -> bool:
        bracket_map = {')': '(', ']': '[', '}': '{'}
        stack = []

        for char in s:
            if char in bracket_map:  # If it's a closing bracket
                # Check if the stack is not empty and the top of the stack matches
                if stack and stack[-1] == bracket_map[char]:
                    stack.pop()
                else:
                    return False
            else:  # If it's an opening bracket
                stack.append(char)

        # If the stack is empty, all brackets are balanced
        return not stack
    
    
sol = Solution()
s1 = "[]"
s2 = "[(])"
s3  = "([{}])"
print(sol.isValid(s1))
print(sol.isValid(s2))
print(sol.isValid(s3))
