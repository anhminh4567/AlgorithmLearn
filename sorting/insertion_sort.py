import random

random_numbers: list[int]   = [random.randint(1, 100) for _ in range(10)]
edge_1: list[int] = [0]
edge_2: list[int] = []
edge_3: list[int] = [2,0]


def insertion_sort(arr: list[int] ):
    if len(arr) == 0 or len(arr) == 1:
        return 
    # according to insetion sort algorithm, we start from the second element and compare it with the first element
    # if the first element is greater than the second element, we swap them
    for i in range(1, len(arr)):
        value = arr[i]
        j = i - 1
        #remember to check for 0 index
        #use while(), since we have to check it agaainst all the previous value
        while j >= 0 and value < arr[j] :
            arr[j + 1] = arr[j]
            #arr[j] = value // we dont place value here, in thee While()
            # only shift, no need to assign value to the previous, do
            # after shifting all correct value
            j -= 1
        arr[j + 1]  = value
        
if __name__ == "__main__":
    print(f"Before: {random_numbers}", end="\n")
    insertion_sort(random_numbers)
    print(f"after:  {random_numbers}",end="\n")
    print("----------edge 1 --------------")
    insertion_sort(edge_1)
    print(edge_1, end="\n")
    print("----------edge 2 --------------")
    insertion_sort(edge_2)
    print(edge_2, end="\n")
    print("----------edge 3 --------------")
    insertion_sort(edge_3)
    print(edge_3, end="\n")    