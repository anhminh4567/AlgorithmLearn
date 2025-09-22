# https://neetcode.io/problems/k-closest-points-to-origin?list=neetcode150
# MEDIUM
'''
You are given an 2-D array points where points[i] = [xi, yi] represents the
coordinates of a point on an X-Y axis plane. You are also given an integer k.

Return the k closest points to the origin (0, 0).

The distance between two points is defined as the Euclidean distance
(sqrt((x1 - x2)^2 + (y1 - y2)^2)).

You may return the answer in any order.
'''
import heapq
from math import sqrt
from typing import List


class Solution:
    '''STANDARD our solution MIN HEAP
    O(n + Log n ) not optimized
    use max heap and sized heap instead
    '''

    def kClosest_heap(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        heap = []
        counter = 0
        for point in points:
            distance = sqrt(point[0] ** 2 + point[1] ** 2)
            heapq.heappush(heap, (distance, point))
        counter = 0
        while counter < k:
            if len(heap) == 0:
                break
            next_min = heapq.heappop(heap)
            result.append(next_min[1])
            counter += 1
        return result

    '''OPTIMIZED MAX_HEAP
    O( n*log K) (expected)
    why n: interate through the points
    why logk: keap a max heap size (k) and each push() or pop() is log(k) 
    k : size we want to return
    n : point size
    '''

    def kClosest_heap_optimized(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            distance = -(point[0] ** 2 + point[1] ** 2)
            heapq.heappush(heap, (distance, point))
            if len(heap) > k:
                heapq.heappop(heap)
        return [point for (_, point) in heap]
    '''SORT :))
    O(n * log(n))
    '''

    def kClosest_SIMPLE(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda p: p[0]**2 + p[1]**2)
        return points[:k]


points = [[0, 2], [2, 0], [2, 2]]
k = 2
print(Solution().kClosest_heap(k, points))
