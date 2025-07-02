

from typing import List


class BinaryTreeAsList():
    @classmethod
    def insert_left(self, parentNode: List, value: str):
        left = parentNode.pop(1)
        if len(left) > 0:
            # this mean if there is a left node and we insert there
            # we add new node, bring the old left to the new left
            parentNode.insert(1, [value, left, []])
        else:
            parentNode.insert(1, [value, [], []])

    @classmethod
    def insert_right(self, parentNode: List, value: str):
        right = parentNode.pop(2)
        if len(right) > 0:
            # this mean if there is a left node and we insert there
            # we add new node, bring the old left to the new left
            parentNode.insert(2, [value, [], right])
        else:
            parentNode.insert(2, [value, [], []])

    @classmethod
    def create_new_tree(self, value):
        return [value, [], []]

    @classmethod
    def getRootVal(self, root):
        return root[0]

    @classmethod
    def setRootVal(self, root, newVal):
        root[0] = newVal

    @classmethod
    def getLeftChild(self, root):
        return root[1]

    @classmethod
    def getRightChild(self, root):
        return root[2]


x = BinaryTreeAsList.create_new_tree('a')
BinaryTreeAsList.insert_left(x, 'b')
BinaryTreeAsList.insert_right(x, 'c')
right_from_root = BinaryTreeAsList.getRightChild(x)
BinaryTreeAsList.insert_right(right_from_root, 'd')
BinaryTreeAsList.insert_left(
    BinaryTreeAsList.getRightChild(right_from_root), 'e')

print(x)
