# https://neetcode.io/problems/permutation-string?list=neetcode150
# Permutation in String
# Solved 
# You are given two strings s1 and s2.

# Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.

# Both strings only contain lowercase letters.

# Example 1:
# Input: s1 = "abc", s2 = "lecabee"

# Output: true


class Solution:
    def checkInclusion_Oursolution_Normal_week(self, s1: str, s2: str) -> bool:
        # check freq
        freq = {}
        for char in s1:
            if char not in freq:
                freq[char] = 1
            else:
                freq[char] += 1

        window_size = len(s1)
        l, r = 0, window_size - 1
        while r < len(s2):
            exist = True
            curr_freq = freq.copy()
            for i in range(l, r + 1):
                if s2[i] not in curr_freq:
                    exist = False                
                    break
                curr_freq[s2[i]] -=1
                if curr_freq[s2[i]] < 0:
                    exist = False
                    break
            if exist:
                return exist
            else:
                l += 1
                r += 1
        return False
    # solution hashtable from solution page
    #Time complexity: O(n∗m)
    # Space complexity: O(1) since we have at most 26 different characters
    def checkInclusion_Hashtable(self, s1: str, s2: str) -> bool:
        count1 = {}
        for c in s1:
            count1[c] = 1 + count1.get(c, 0)
        
        need = len(count1)
        for i in range(len(s2)):
            count2, cur = {}, 0
            for j in range(i, len(s2)):
                count2[s2[j]] = 1 + count2.get(s2[j], 0)
                if count1.get(s2[j], 0) < count2[s2[j]]:
                    break
                if count1.get(s2[j], 0) == count2[s2[j]]:
                    cur += 1
                if cur == need:
                    return True
        return False
    #   BEST SOLUTION, THE LOGIC HERE CAN BE USED ELSE WHERE, the TRACKING LOGIC 
    # (match) + the Counter logic (s1Counter,s2Counter)
    # BEST solution, for speed and space, complex shit
    # Time complexity: O(n)
    # Space complexity: O(1)
    # the idea is in the clip
    # first check the count of each char of s1, then s2
    # THEN for only 1 first check where we check 26 char from a->z
    # like s1 = abc then its counter is [1,1,1,0,0...]
    # we check 26 char for both s1 and s2 array count, if they equal in count value => they match
    # => match 24 if s2 contain 2 char have same count (26 - 2 char that == s1 count)
    #       next
    #   now slide 1 index, remove the count on L window, re-compare the count for that 
    # char index [ using ord('char') - ord('a') ]
    #   if count is no longer equal for both from s1 and s2 counter array => match -=1 else match +=1
    #       FINALLY
    # if match is 26, means all character counter is match => true
    def checkInclusion_BEST_ALL(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26
                
       
       
print(Solution().checkInclusion_Hashtable("abcdxabcde","abcdeabcdx")) 