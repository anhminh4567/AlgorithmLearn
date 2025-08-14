# https://leetcode.com/problems/repeated-dna-sequences/?envType=problem-list-v2&envId=sliding-window
# the DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

# For example, "ACGAATTCCG" is a DNA sequence.
# When studying DNA, it is useful to identify repeated sequences within the DNA.

# Given a string s that represents a DNA sequence, return 
# all the 10-letter-long sequences (substrings) that occur more than once in a
# DNA molecule. You may return the answer in any order.

# Example 1:

# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# Output: ["AAAAACCCCC","CCCCCAAAAA"]
# Example 2:

# Input: s = "AAAAAAAAAAAAA"
# Output: ["AAAAAAAAAA"]
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        result = set()
        countered = set()
        windowSize = 10
        for i in range(0, len(s) - windowSize  + 1):
            sub = s[i:i + windowSize]
            if sub in countered:
                result.add(sub)
            else:
                countered.add(sub)
        return list(result)

print(Solution().findRepeatedDnaSequences("AAAAAAAAAAA"))