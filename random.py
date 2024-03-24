"""
these are questions I had a tough time answering during interviews
    Questions to work on:
        - algorithm for amount of deletions between two strings
        - given a long int -> 10002304001, how many different ways can you write this
            - if each num in int corresponds to letter in alphabet 0:a 1:b 2:c ... z:25 (CISCO)
        - given an array of ints and an int x := segment size
            - get the minimum in segment
            - return maximum of the segments
        - textformatting(start: List[int], end: List[int], style: List[char]) -> int:
            - calculate the minimum number of operations to be done
            - selection + 1 operation, styling + 1 operation
            - take account for ranges that are similar
                - not sure if i should take account only for consecutive ranges or ranges in the whole list
"""

def consecutiveHighLows(test):
    """ 
        Given an array of ints 
        return the longest consecutive highs or consecutive lows:
        [1,2,3,4] -> 4
        [1,3,2,1,4,5] -> 3 (3,2,1) or (1,4,5)
        Solved it pretty fast rn, but during the test I didnt fully understand the question well enough

    """
    upCount = 1
    downCount = 1
    upMax = 0
    downMax = 0
    index = 0
    while(index < len(test)-1):
        if(test[index] < test[index + 1]): # going up
            upCount += 1
            downMax = max(downCount, downMax)
            downCount = 1
        elif(test[index] > test[index + 1]): # going down
            downCount += 1
            upMax = max(upCount, upMax)
            upCount = 1
        else:
            downMax = max(downCount, downMax)
            upMax = max(upCount, upMax)
            downCount = 1
            upCount = 1
        index += 1
    upMax = max(upMax, upCount)
    downMax = max(downMax, downCount)        
    return max(upMax, downMax)



print(consecutiveHighLows([1,2,3,4]))
print(consecutiveHighLows([1,3,2,1,4,5]))
print(consecutiveHighLows([1,3,2,2,0,1,4,5]))