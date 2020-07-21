def pprint(matrix):
    """ this just prints the matrix in a readable way """
    for i, row in enumerate(matrix):
        print(i ,row, end=",\n") 

def islandProblem():
    """
    the idea is to iterate through the matrix mark visited nodes and check its neighbours
    continue to iterate through the neighbours, once there are no more neighbours to iterate through
    then you have found an island island
    then continue to iterate through the matrix unntil you find another unvisited node and repeat previous steps

    right now just try to find number of islands, numOfIslands++ each time a node of clusters is found
    in my programming interview i was asked to find the largest Island given a matrix:
        to do this all you really need is a variables maxIslandSize, currentIslandSize
        currentIslandSize++ when checking for neighbours
        once there are no more neighbours (queue is empty), maxIslandSize = currentIslandSize > maxIslandSize ? currentIslandSize : maxIslandSize

    need to handle boundary cases: (this is actually entirely dependent on where the starting node is)
        (if the starting node is the first index of the matrix then you do not really need to worry about the boundary, because the matrix is always going to be looking from top left to bottom right
        this is also dependent on whether or not diagonal indexes are considered islands 
        )
        (if the starting node is handpicked and is not guaranteed to be the first index of the matrix then you will have to worry about the boundaries. This is because if it is handpicked, there is not really any way of telling whether or not you start from in the middle of the island or at the edge of an island)

        if i = 0 or i = (heightOfMatrix - 1) i.e. (first and last row)
        if j = 0 or j = (widthOfMatrix - 1)  i.e. (first and last col) 
        it can be either or, or both
        if i == (heightOfMatrix - 1) && j == 0: (this is a corner) (i++,j), (i, j++), (i++,j++)
        if i == 0 && j == 0: (i--, j), (i++, j), (i--,j++), (i, j++) etc.

        also good to note that bfs can also work on trees. It is a good reminder that when iterating through bfs the parent child
        relationship is arbitrary and varies from problem to problem. For example a parent child relationship is different from this
        problem to something like an adjacency matrices where in adjacency matrices it is a lot easier to find the child positions
        in this case you would have to iterate through the surrounding neighbors and making sure you are not out of bounds.
    """
    testCase = [
        [1,1,0,0,0,1,0,0,1],
        [1,1,0,0,0,1,0,1,0],
        [1,0,0,0,0,1,0,1,1],
        [1,1,0,0,0,1,0,1,0],
        [1,1,0,0,1,1,0,0,0]
    ]
    # number of islands in here is 3
    # biggest island here is 9
    # to keep track of visited nodes so that it is in place, make it -1, this makes it so that you dont have to keep a list of visited nodes
    lenOfRow = len(testCase[0]) # i am assuming that the matrix is not empty, and that the rows are not empty
    numOfCols = len(testCase) # also assuming that the matrix is not empty
    print(lenOfRow, numOfCols)
    numOfIslands = 0 
    largestIsland = 0
    for i, row in enumerate(testCase):
        for j, num in enumerate(row):
            q = []
            if num == 1:
                q.append((i, j))
                some = 0
                trackIslandSize = 0
                while q:
                    currI, currJ = q.pop(0) # pop() usually defaults to the last element of a list
                                            # but since this is a queue we want to get FIFO (first element)
                    testCase[currI][currJ] = -1
                    for indexOp in range(-1,2): # this is to help check for neighboring nodes. Also ranges in python are [inclusive, exclusive)
                        checkI = currI + indexOp
                        # think about whether or not you can go out of bounds of x but not go out of bounds of y
                        # and how to solve it, im pretty sure above is true
                        # i should probably have a check for x and then have another for loop for y
                        if checkI >= 0 and checkI < numOfCols:
                            for yIndexOp in range(-1,2):
                                checkJ = currJ + yIndexOp
                                if checkJ >= 0 and checkJ < lenOfRow:
                                    # i check to see whether or not the neighboring node has been visited, and to see if 
                                    # it is already in the q. 
                                    # i feel like there is a way to do it without having to check if it is in q
                                    # i could probably just have a check to see whether or not the current value is -1, 1
                                    # i think the better way to do this is just change the value of the node to be like 2 (which means it is in queue but no visisted), will need to change logic around for this tho
                                    # if value is 2, then that means the node is in q
                                    # this assumes that the original values of the array is just 0,1
                                    if testCase[checkI][checkJ] == 1:
                                        q.append((checkI,checkJ))
                                        testCase[checkI][checkJ] = 2
                    print(q)
                    pprint(testCase)
                    some += 1
                    trackIslandSize += 1
                numOfIslands += 1 
                if largestIsland < trackIslandSize: 
                    largestIsland = trackIslandSize

    print("Largest Island Size", largestIsland)
    return numOfIslands
         
def tree():
    """ this is to learn tree traversal """ 
    

if '__name__' == '__main__':
    print('Number of Islands', islandProblem())
