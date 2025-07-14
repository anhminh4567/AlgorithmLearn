import sys
from typing import Optional


# print(sys.path)
a: list[int] = [ 1, 3 , 6 , 4 ,1 ,2 ]
a.sort()
print(a)
for val in a:
    print(val)
    pass


def sol(A : list[int]) -> int:
    smallest = 1
    for i in A:
        if i == smallest:
            smallest += 1
    return smallest    
        
print(sol(a))  # 5



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.df_validTree(root, None,None)
                         
        
    def df_validTree(self, root: Optional[TreeNode], _min: Optional[int], _max : Optional[int] ):
        if _min is not None and root.val <= _min :
            return False
        if _max is not None and root.val >= _max:
            return False
        leftValid, rightValid = True, True
        if root.left:
            leftValid = self.df_validTree(root.left, _min , root.val)
        if root.right:
            rightValid = self.df_validTree(root.right, root.val, _max)

        return leftValid and rightValid


node1 = TreeNode(0)
node2 = TreeNode(-1)
node1.right = node2
Solution().isValidBST(node1)
        
        

def lengthOfLongestSubstring(s: str) -> int:
        left = 0 
        right = 0 
        result = 0
        
        if len(s) < 1:
            return 0
        char_set = set()
        while right < len(s):
            cur_char = s[right]
            if cur_char not in char_set:
                char_set.add(cur_char)
                result = max(result, right - left + 1)
            else:
                while True:
                    left_char = s[left]
                    if left_char != cur_char:
                        left +=1
                        
                        continue
                    else:
                        left +=1
                        break
            right += 1

        return result
print(lengthOfLongestSubstring("tmmzuxt"))
print(list(range(0,1)))

def checkInclusion( s1: str, s2: str) -> bool:
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
checkInclusion("adc","dcda")


def checkInclusion( s1: str, s2: str) -> bool:
    # freq of s1 then s2
    freq_s1 = {}
    for c in s1:
        freq_s1[c] = freq_s1.get(c,0) + 1
    expected = len(freq_s1)
    l = 0
    r = l + len(s1) -1
    while r < len(s2):
        freq_s2 = {}
        counter = 0
        for i in range(l, r + 1):
            freq_s2[s2[i]] = freq_s2.get(s2[i],0) + 1
            if freq_s1.get(s2[i],0) < freq_s2[s2[i]]:
                break
            if freq_s1.get(s2[i],0) == freq_s2[s2[i]]:
                counter += 1
            if counter == expected:
                return True
        l += 1
        r += 1
        
    return False

print(checkInclusion("abcdxabcde","abcdeabcdx"))