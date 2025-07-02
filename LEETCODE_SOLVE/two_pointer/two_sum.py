from ast import List, Tuple


sortedArray = [10, 20, 30, 40, 50, 80, 90]
sum = 70


pairResult: list[tuple] = []


def findSumPair(k: int, arr: list[int] = []) -> None:
    if arr is None or len(arr) == 0:
        return
    if len(arr) < 1:
        return
    left = 0
    right = len(sortedArray) - 1
    while left < right:
        sum = sortedArray[left] + sortedArray[right]
        if sum == k:
            pairResult.append((sortedArray[left], sortedArray[right]))
            left += 1
            right -= 1
        elif sum < k:
            left += 1
            continue
        elif sum > k:
            right -= 1
            continue
        else:
            pass


findSumPair(sum, sortedArray)

print(pairResult)
