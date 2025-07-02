from typing import Optional


array_1: list[int] = [1,1,2,3,3,3,4,4] #sorted
array_2: list[int] = [4,4,4,5,5,6,7,7]#sorted


def merge_sorted_arrays(firstArr: list[int], secondArr: list[int]) -> list[int]:
    prev: Optional[int] = -1
    firstPos : Optional[int] = 0
    secondPos : Optional[int] = 0
    runCount : int = 1
    result: list[int] = []
    
    while True :
        firstVal : Optional[int] = None
        secondVal : Optional[int] = None
   
        if firstPos < len(firstArr):
            firstVal = firstArr[firstPos]
        if  secondPos < len(secondArr):
            secondVal = secondArr[secondPos]
        
        if firstVal is None and secondVal is None:
            print('done loop')
            break
        
        if firstVal is None :
            if secondVal > prev:
                result.append(secondVal) 
                prev = secondVal
                secondPos += 1
            else:
                secondPos +=1
            continue
            
            
        if secondVal is None :
            if  firstVal > prev:
                result.append(firstVal)
                prev = firstVal
                firstPos +=1
            else :
                secondPos +=1    
            continue

        if firstVal < secondVal :
            if firstVal > prev:
                result.append(firstVal)
                prev = firstVal
                firstPos += 1
            else: # when the firtVal = prev
                firstPos += 1
             
        if secondVal <= firstVal :
            if secondVal > prev:
                result.append(secondVal)
                prev = secondVal
                secondPos +=1
            else:
                secondPos +=1
            
        runCount +=1
    
    print(runCount)
    return result
    
    
if __name__ == "__main__":
    print("start")
    res: list[int]   = merge_sorted_arrays(array_1,array_2)
    print(res)