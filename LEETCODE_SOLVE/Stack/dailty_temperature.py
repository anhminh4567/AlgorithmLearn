# https://neetcode.io/problems/daily-temperatures
# You are given an array of integers temperatures where temperatures[i]
# represents the daily temperatures on the ith day.

# Return an array result where result[i] is the number of days
# after the ith day before a warmer temperature appears on a future day.
# If there is no day in the future where a warmer temperature will appea
# r for the ith day, set result[i] to 0 instead.


# Recommended Time & Space Complexity
# You should aim for a solution as good or better than O(n) time and O(n) space,
# where n is the size of the input array.


from calendar import c


temperatures = [30, 38, 30, 36, 35, 40, 28]  # [1,4,1,2,1,0,0]
temperatures2 = [22, 21, 20]  # [0,0,0]
temperatures3 = [89, 62, 70, 58, 47, 47, 46,
                 76, 100, 70]  # [8,1,5,4,3,2,1,1,0,0]


class Solution:
    # This is a flawless soltution, BUT WE DID NOT SOLVE IT BY OURSELF
    # this shit is copied from solution, LOSER
    def dailyTemperatures_mystack(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackTtemp, stackIndex = stack.pop()
                res[stackIndex] = i - stackIndex
            stack.append((t, i))
        return res

    def dailyTemperatures_Brute(self, temperatures: list[int]) -> list[int]:
        '''
        this is a loser solution, use brute force, O(n^2) time complexity
        '''
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            totalDayBeforeWarmer = 0
            maxTemp = temperatures[i]
            j = i + 1
            while j < len(temperatures):
                if temperatures[j] > maxTemp:
                    totalDayBeforeWarmer += 1
                    break
                else:
                    totalDayBeforeWarmer += 1
                j += 1
            if j == len(temperatures):
                totalDayBeforeWarmer = 0
            result[i] = totalDayBeforeWarmer
        return result

def test( temperatures: list[int]) -> list[int]:
    result = [0] * len(temperatures)
    for i in range(len(temperatures)):
        totalDayBeforeWarmer = 0
        j = i + 1
        for j in range(j , len(temperatures) + 1):
            if j == len(temperatures):
                break
            if temperatures[j] > temperatures[i]:
                totalDayBeforeWarmer += 1
                break
            else:
                totalDayBeforeWarmer += 1
        if j == len(temperatures) :
            totalDayBeforeWarmer = 0
        result[i] = totalDayBeforeWarmer
    return result

sol = Solution()
# print(sol.dailyTemperatures_Brute(temperatures))  # [1,4,1,2,1,0,0]
# print(sol.dailyTemperatures_Brute(temperatures2))  # [0,0,0]
# print(sol.dailyTemperatures_Brute([]))  # []
print(sol.dailyTemperatures_mystack(temperatures))  # [1,4,1,2,1,0,0]
print(sol.dailyTemperatures_mystack(temperatures2))  # [0,0,0]
print(sol.dailyTemperatures_mystack([]))  # []
print(sol.dailyTemperatures_mystack(temperatures3))  # []

print("-------")
print(test(temperatures))  # [1,4,1,2,1,0,0]
print(test(temperatures2))  # [0,0,0]
print(test([]))  # []
print(test(temperatures3))  # []
