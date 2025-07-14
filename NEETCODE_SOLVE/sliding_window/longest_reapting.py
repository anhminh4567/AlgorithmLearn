# https://neetcode.io/problems/longest-repeating-substring-with-replacement?list=neetcode150
# Longest Repeating Character Replacement
# You are given a string s consisting of only uppercase english characters 
# and an integer k. You can choose up to k characters of the string and replace
# them with any other uppercase English character.

# After performing at most k replacements, return the length of the longest
# substring which contains only one distinct character.

import random
class Solution:
    # homeade solution (O(n) speed and memory , o(26n))
    # hell yea
    # solution, go through the list, check for unique char and count freq {} (the freq is extra no use)
    # after the unique char in list => 
    # => interate through each key , using sliding window, LEFT RIGHT, and move it
    # move logic:
    #      1. if the R window is == current char => it dont need to use the replacement in K given
    #      BUT if R != char => it has to replace this char with the same current_char => lost -1 replacementK
    #      2. incase we run out of replacement given at the R += 1 => now the max is set, we move the L window
    #      3. L window, move, if == current_char => we dont account for replacement
    #      ELSE, != current_char => this position WAS REPLACED when we move the R window => replacementK += 1 (we basically
    #  giving the replacement back to the list, UNTIL THE REPLACEMENT >= 0, minimal window == K
    def characterReplacement_self_solve_HELL_YEA(self, s: str, k: int) -> int:
        # result = random.randint(1,2)
        if len(s) <= 2:
            return 2
        freq: dict[str,int]  = {}
        #count the highest frequency of char
        for i in range(0, len(s)):
            char = s[i]
            if char not in freq:
                freq[char] = 1
            else:
                freq[char] += 1
        max_per_char = {}
        for char in freq.keys():
            replaceLeft = k
            max_per_char[char] = 0
            left = 0
            right = 0
            while right < len(s):
                if s[right] == char:
                    max_per_char[char] = max(max_per_char[char], right - left + 1)    
                else:
                    replaceLeft -= 1
                    while replaceLeft < 0:
                        if s[left] != char:                        
                            replaceLeft += 1
                        left += 1
                    max_per_char[char] = max(max_per_char[char], right - left + 1)    
                right += 1
        
        return max(max_per_char.values())
    # o(26n worsecase)
    # mcuh easier than our solution
    def characterReplacement_standard(self, s: str, k: int) -> int:
        res = 0
        charSet = set(s)

        for c in charSet:
            count = l = 0
            for r in range(len(s)):
                if s[r] == c:
                    count += 1

                while (r - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1
                    
                res = max(res, r - l + 1)
        return res
    
    # most optimial solution on neetcode
    # KEY INSIGHT
    # main logic, the sliding 
    def characterReplacement_OPTIMAL(self, s: str, k: int) -> int:
        count = {}     # Track frequency of each character in current window
        res = 0        # Track maximum valid substring length
    
        l = 0          # Left pointer of window
        maxf = 0       # Maximum frequency of any character in current window
        for r in range(len(s)):  # Right pointer of window
            # Add current character to frequency counter
            count[s[r]] = 1 + count.get(s[r], 0)
            # Update the maximum frequency
            maxf = max(maxf, count[s[r]])
            # KEY INSIGHT: if window size minus most frequent character count > k,
            # we need more than k replacements, so shrink window
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            # Update result with current valid window size
            res = max(res, r - l + 1)
        return res