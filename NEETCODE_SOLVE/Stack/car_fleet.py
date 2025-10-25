# https://neetcode.io/problems/car-fleet?list=neetcode150
# MEDIUM
'''
There are n cars traveling to the same destination on a one-lane highway.

You are given two arrays of integers position and speed, both of length n.

position[i] is the position of the ith car (in miles)
speed[i] is the speed of the ith car (in miles per hour)
The destination is at position target miles.

A car can not pass another car ahead of it. It can only catch up to another 
car and then drive at the same speed as the car ahead of it.
A car fleet is a non-empty set of cars driving at the same position and same
speed. A single car is also considered a car fleet.
If a car catches up to a car fleet the moment the fleet reaches the
destination, then the car is considered to be part of the fleet.
Return the number of different car fleets that will arrive at the destination.

Example 1:
Input: target = 10, position = [1,4], speed = [3,2]
Output: 1
Explanation: The cars starting at 1 (speed 3) and 4 (speed 2) become a fleet, meeting each other at 10, the destination.

Example 2:
Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]
Output: 3
Explanation: The cars starting at 4 and 7 become a fleet at position 10. 
The cars starting at 1 and 0 never catch up to the car ahead of them. 
Thus, there are 3 car fleets that will arrive at the destination.
'''


from typing import List

# we did not solve this


class Solution:
    '''
    suggested by sonnet 
    very good explanation , especially the Stack part
    '''

    def carFleet_stack(self, target: int, position: List[int], speed: List[int]) -> int:
        # Create pairs of (position, speed) and sort by position in descending order
        cars = list(zip(position, speed))
        cars.sort(reverse=True)  # Sort by position (closest to target first)

        stack = []

        for pos, spd in cars:
            time_to_reach = (target - pos) / spd

            # If this car takes longer to reach than the car in front,
            # it will form its own fleet
            if not stack or time_to_reach > stack[-1]:
                stack.append(time_to_reach)
        return len(stack)

    def carFleet_iteration(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)

        fleets = 1
        prevTime = (target - pair[0][0]) / pair[0][1]
        for i in range(1, len(pair)):
            currCar = pair[i]
            currTime = (target - currCar[0]) / currCar[1]
            if currTime > prevTime:
                fleets += 1
                prevTime = currTime
        return fleets


# print(Solution().carFleet(10, position=[4, 1, 0, 7], speed=[2, 2, 1, 1]))
# print(Solution().carFleet(100, position=[0, 2, 4], speed=[4, 2, 1]))
print(Solution().carFleet(10, position=[0, 4, 2], speed=[2, 1, 3]))
