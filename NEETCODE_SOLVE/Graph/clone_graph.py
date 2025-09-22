# https://neetcode.io/problems/clone-graph?list=neetcode150
# Medium

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


from collections import deque
from typing import Optional


class Node:
    def __init__(self, val: int = 0, neighbors: Optional[list['Node']] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    # There are 2 solution to this
    # 1. DFS
    # 2. BFS
    # we are using BFS
    # DFS work quite similar
    # Shared: track the visited with a dictionary (or set() depends), create a copy and store in
    # that tracker
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        cloneed_hash = dict[Node, Node]()
        copy = Node(node.val)
        cloneed_hash[node] = copy
        queue = deque([node])

        while queue:
            cur = queue.popleft()
            for nei in cur.neighbors:
                if nei not in cloneed_hash:
                    nei_copy = Node(nei.val)
                    cloneed_hash[nei] = nei_copy
                    queue.append(nei)
                cloneed_hash[cur].neighbors.append(cloneed_hash[nei])
        return copy


sol = Solution()

node1 = Node(1, [])
node3 = Node(3, [])
node2 = Node(2, [node1, node3])
node1.neighbors.append(node2)
node3.neighbors.append(node2)

print(sol.cloneGraph(node1).neighbors)
