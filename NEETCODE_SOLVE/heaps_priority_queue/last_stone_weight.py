# https://neetcode.io/problems/last-stone-weight?list=neetcode150
# Difficulty: Easy
# this is just mostly to use the bulit in library, get used to the heapq library
# You are given an array of integers stones where stones[i] represents the weight of the ith stone.

# We want to run a simulation on the stones as follows:

# At each step we choose the two heaviest stones, with weight x and y and smash them togethers
# If x == y, both stones are destroyed
# If x < y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# Continue the simulation until there is no more than one stone remaining.

# Return the weight of the last remaining stone or return 0 if none remain.


import heapq
from typing import List


class Solution_Our:

    def lastStoneWeight(self, stones: List[int]) -> int:
        # create a max heap
        heapq._heapify_max(stones)
        while len(stones) > 1:
            biggest = heapq._heappop_max()
