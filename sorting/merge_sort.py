# it is of type Divide_And_Conquer
import math
import random


def mergeSort(arr: list[int] ) -> list[int]:
    if len(arr) <= 1:
        return arr
    
    mid = math.floor( len(arr) / 2)
    subLeft = arr[:mid] # from start to mid, not include mid
    subRight = arr[mid:]
    
    sortedSubLeft = mergeSort(subLeft)
    sortedSubRight = mergeSort(subRight)
    
    return merge(sortedSubLeft, sortedSubRight)
    
    
def merge(subLeft: list[int], subRight: list[int]):
    # init new array to store merged
    result = []
    # init 2 pointer to traverse the 2 sub arrray
    i = 0
    j = 0
    while i < len(subLeft) and j < len(subRight):
        if subLeft[i] < subRight[j]:
            result.append(subLeft[i])
            i += 1
        else:
            result.append(subRight[j])
            j += 1
    # after the above step, the list is still missing, since
    # not all item is append() , we have to append the remaining if the
    # one of 2 subArray still have value
    # There MUST be 1 sub array still have value ( think about it, impossible
    # to have 2 sub array finish all at same time )
    result.extend(subLeft[i:])    
    result.extend(subRight[j:])
    
    return result       
    
    
if __name__ == "__main__":
    random_numbers: list[int]   = [random.randint(1, 100) for _ in range(10)]
    edge_1: list[int] = [0]
    edge_2: list[int] = []
    edge_3: list[int] = [2,0]
    print(f"before: {random_numbers}")
    sortedArray = mergeSort(random_numbers)
    print(f"result: {sortedArray}")
    print("----------edge 1 --------------")
    sortedEdge1 = mergeSort(edge_1)
    print(sortedEdge1, end="\n")
    print("----------edge 2 --------------")
    sortedEdge2 = mergeSort(edge_2)
    print(sortedEdge2, end="\n")
    print("----------edge 3 --------------")
    sortedEdge3: list[int] = mergeSort(edge_3)
    print(sortedEdge3, end="\n")  
    
    
# dictionary = {"a": 1, "b": 2, "c": 3, "d": 4}
# for k,v in dictionary.items():
#     print(f"{k} : {v}")