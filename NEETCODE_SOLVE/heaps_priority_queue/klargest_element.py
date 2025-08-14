# https://neetcode.io/problems/kth-largest-integer-in-a-stream?list=neetcode150
# LEVEL : Easy 
import heapq
from typing import List

# use min heap ( our approach using pure implementation)
class KthLargest_self_solve:
    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        self.build_heap(self.heap)

    def parent(self,index):
        return (index - 1) // 2 
    def leftChild(self, index):
        return index * 2 + 1
    def rightChild(self, index):
        return index * 2 + 2
    def add(self, val: int) -> int:
        self.heap.append(val)
        self.heapify_up(len(self.heap) - 1)
        if len(self.heap) > self.k:
            self.pop()
        return self.heap[0]
        
    def pop(self):
        self.heap[0], self.heap[-1] = self.heap[-1] , self.heap[0]
        self.heap.pop()
        self.heapify_down(0)

    def build_heap(self,array: List[int]):
        middle_idx = (len(array) // 2) - 1
        for i in range(middle_idx, -1,-1):
            self.heapify_down(i)
        while len(self.heap) > self.k:
            self.pop()
    # build max heap ( best is min heap with size K)
    # this always start  at root and go down till then end of the list
    # WRONG NOT WORK NOW
    def heapify_down(self, index):
        list_len = len(self.heap)
        largest_index = index 
        while True:
            left_idx = self.leftChild(index)
            right_idx = self.rightChild(index)
            if left_idx < list_len and self.heap[left_idx] < self.heap[largest_index]: 
                largest_index = left_idx
            if right_idx < list_len and self.heap[right_idx] < self.heap[largest_index]:
                largest_index = right_idx
            if largest_index != index:
                #swap 
                self.heap[index], self.heap[largest_index] = self.heap[largest_index], self.heap[index]
                index = largest_index
            else:
                break
    # min heap so child > parent
    def heapify_up(self, index):
        while index > 0:
            parent_idx = self.parent(index)
            if parent_idx == 0 and self.heap[index] >= self.heap[parent_idx]:
                break
            if self.heap[parent_idx] > self.heap[index]:
                self.heap[parent_idx] , self.heap[index] = self.heap[index] , self.heap[parent_idx]
                index = parent_idx
            else:
                break
    
test  = KthLargest_self_solve(3, [1, 2, 3, 3])
print(test.add(3))
print(test.add(5))
print(test.add(6))
print(test.add(7))
print(test.add(8))
print("-------------")
test2  = KthLargest_self_solve(1, [1, 2, 2, 2, 2, 3])
print(test2.add(4))  # Should print the largest after adding 4
print(test2.add(2))  # Should print the largest after adding 2
print(test2.add(5))  # Should print the largest after adding 5



# SOLUTION from neetcode
# very elegent, using built in heap
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]