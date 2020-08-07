"""
these are questions I had a tough time answering during interviews
    Questions to work on:
        - algorithm for amount of deletions between two strings
        - 
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