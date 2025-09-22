# https://leetcode.com/problems/minimum-time-visiting-all-points/

# On a 2D plane, there are n points with integer coordinates points[i] = [xi, yi]. Return the minimum time in seconds to visit all the points in the order given by points.

# You can move according to these rules:

# In 1 second, you can either:
# move vertically by one unit,
# move horizontally by one unit, or
# move diagonally sqrt(2) units (in other words, move one unit vertically then one unit horizontally in 1 second).
# You have to visit the points in the same order as they appear in the array.
# You are allowed to pass through points that appear later in the order, but these do not count as visits.


# MAJOR HINT
# -> Calculate the maximum between abs(x1 -x2) and abs(y1 - y2)
# why? because move diagonal or horizontal or vertical is the same time
# you can move +1,+1  +1,-1,  -1,+1   -1,-1
# => you dont need to know which direction, just know the maxium between 2 distance

from typing import List


class Solution:
    def minTimeToVisitAllPoints_selfSolve(self, points: List[List[int]]) -> int:
        res = 0

        def executeMove(start: List[int], target: List[int]):
            time = 0
            x1, y1 = start[0], start[1]
            x2, y2 = target[0],target[1]
            while x1 != x2 or y1 != y2:
                if x1 < x2 and y1 < y2:
                    x1 +=1
                    y1 +=1
                elif x1 < x2 and y1 > y2:
                    x1 +=1
                    y1 -=1
                elif x1 < x2 and y1 == y2:
                    x1 +=1
                elif x1 > x2 and y1 < y2:
                    x1 -=1
                    y1 +=1
                elif x1 > x2 and y1 > y2:
                    x1 -=1
                    y1 -=1
                elif x1 > x2 and y1 == y2:
                    x1 -=1
                elif x1 == x2 and y1 < y2:
                    y1 +=1
                elif x1 == x2 and y1 > y2:
                    y1 -=1
                time +=1
            return time
        if len(points) <=1:
            return 0
        start = points.pop()
        while len(points) != 0:
            target = points.pop()
            res += executeMove(start,target)
            start = target
        return res
            
        
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        # get the last pos (because it does not matter at start or stop, just follow the order)
        res = 0
        x1,y1 = points.pop()
        
        while len(points) != 0:
            x2 ,y2 = points.pop()
            res += max(abs(x1 - x2),abs(y1 -y2))
            x1 , y1 = x2,y2
        return res
        
 
sol = Solution(); 
 
 
print(sol.minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]) )
print(sol.minTimeToVisitAllPoints([[3,2],[-2,2]]))

print(sol.minTimeToVisitAllPoints_selfSolve([[1,1],[3,4],[-1,0]]) )
print(sol.minTimeToVisitAllPoints_selfSolve([[3,2],[-2,2]]))

 