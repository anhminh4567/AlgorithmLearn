# https://neetcode.io/problems/string-encode-and-decode?list=neetcode150
# MEDIUM
# Encode and Decode Strings
# Design an algorithm to encode a list of strings to a single string.
# The encoded string is then decoded back to the original list of strings.

# Please implement encode and decode
# Example 1:
# Input: ["neet","code","love","you"]
# Output:["neet","code","love","you"]

# Example 2:
# Input: ["we","say",":","yes"]
# Output: ["we","say",":","yes"]
# Hint 1
# A naive solution would be to use a non-ascii character as a delimiter. Can you think of a better way?
# Hint 3
# We can use an encoding approach where we start with a number representing the length of the string,
# followed by a separator character (let's use # for simplicity), and then the string itself.
# To decode, we read the number until we reach a #, then use that number to read the specified
# number of characters as the string.
from typing import List


class Solution:
    # the most important is PUT NUMBER BEFORE #
    # if put behind then it will mix with words
    # but put before like 22#.... then we dont mix since the next work we know the length already
    # we wont clash the next word seperator and number
    def encode(self, strs: List[str]) -> str:
        res = ""
        for chars in strs:
            count = len(chars)
            res += str(count) + "#" + chars
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            origin = ""
            count_str = ""
            while s[i] != "#":
                count_str += s[i]
                i += 1
            length = int(count_str)
            i += 1
            to = i + length
            origin += s[i:to]
            i = to
            res.append(origin)
        return res


strs = ["we", "say", ":", "yes"]
print(Solution().decode(Solution().encode(strs)))
strs = ["neet", "code", "love", "you"]
print(Solution().decode(Solution().encode(strs)))
