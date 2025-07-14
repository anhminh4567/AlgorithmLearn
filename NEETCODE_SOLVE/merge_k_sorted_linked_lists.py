# https://neetcode.io/problems/merge-k-sorted-linked-lists
# Definition for singly-linked list.
from configparser import SectionProxy
from typing import Optional

#NOTE FROM CHAT GPT
#No, your current implementation of mergeKLists() does not fully meet
# the requirement of achieving O(n * log(k)) time complexity.
# While your implementation achieves O(1) space complexity,
# the time complexity is O(n * k), which is less efficient than the
# optimal solution
# ====> we reach the Recommendation From LeetCode
# which is O ( n * k ) [n: ist toal of nodes, k: is total of link list]
# O(1) space
# ====> NOICE
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0 :
            return None
        if len(lists) == 1:
            return lists[0]
        
        i = 1
        while i < len(lists):
            j = i -1
            curNode = lists[i]
            prevNode = lists[j]
            newNode = self.merge2List(curNode,prevNode)
            lists[i] = newNode
            lists[j] = None
            i += 1
            # note : pop(0) is O(n)
            # pop(-1) is 0(1)  
            # after we done we have list [None,None,Head]
            # just pop() it is O(1) and return head
        return lists.pop()
            
    def merge2List(self, firstLink: ListNode , secondLink: ListNode) -> Optional[ListNode]:
        if firstLink is None and secondLink is None:
            return None
        if firstLink is None:
            return secondLink
        if secondLink is None: 
            return secondLink
        
        headNode : Optional[ListNode] = None
        currentNode : Optional[ListNode ] = None
        if firstLink.val < secondLink.val:
            headNode = firstLink
            currentNode = firstLink
            firstLink = firstLink.next
        else :
            headNode = secondLink
            currentNode = secondLink
            secondLink = secondLink.next
        while firstLink is not None and secondLink is not None:
            if firstLink.val < secondLink.val:
                currentNode.next = firstLink
                currentNode = currentNode.next
                firstLink = firstLink.next
            else :
                currentNode.next = secondLink
                currentNode = currentNode.next
                secondLink = secondLink.next
        
        if firstLink is not None:
            currentNode.next = firstLink
        if secondLink is not None:
            currentNode.next = secondLink
        return headNode
                
                
        

    
        
def list_to_listnode(arr):
    """Helper function to convert a list of integers to a ListNode."""
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

if __name__ == "__main__":
    lists=[[1,2,4],[1,3,5],[3,6]]
    listnodes = [list_to_listnode(sublist) for sublist in lists]
    solution = Solution()
    merged_head: ListNode | None = solution.mergeKLists(listnodes)
    if isinstance(merged_head, ListNode):
        print(merged_head.val, end="\n")
        current = merged_head.next
        while current is not None:
            print(current.val)
            current = current.next
    