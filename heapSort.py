import random

def parent(parentPosition):
    return parentPosition // 2


def leftChild(leftPosition):
    return leftPosition * 2


def rightChild(rightPosition):
    return (rightPosition * 2) + 1


def Leaf(list, position):
    if position >= (len(list)) // 2 and position <= (len(list)):
        return True
    return False


def swap(list, position1, position2):
	temp = list[position1]
	list[position1] = list[position2]
	list[position2] = temp


def minHeapify(list, position):
    if not Leaf(list, position):
        if list[position] > list[leftChild(position)] or list[position] > list[rightChild(position)]:
            if list[leftChild(position)] < list[rightChild(position)]:
                swap(list, position, leftChild(position))
                minHeapify(list, leftChild(position))
            else:
                swap(list, position, rightChild(position))
                minHeapify(list, rightChild(position))


def insertElement(list, num):
    list.append(num)
    current = len(list)
    while list[current] < list[parentPosition(current)]:
        swap(list, current, parentPosition(current))
        current = parentPosition(current)

def removeMin(list):
    temp = list[0]
    # list[-1] gets the last element of the list    
    list[0] = list[-1]
    # deletes the last element of the list
    del list[-1]
    # have to call minheap again because numbers were moved around
    minHeapify(list, 0)
    return temp

def buildMinHeap(list):
	# range(start, stop, step)
    for position in range(len(list) // 2, -1, -1):
        minHeapify(list, position)

def printMinHeap(list, newlist):
    # i initalized temp here so that i dont have to keep initializing it in while loop
    temp = None
    while list:
        temp = removeMin(list)
        print(temp)
        newlist.append(temp)

def main():
    array = [random.randint(0, 100) for i in range(50)]
    # one way to do it without having to use deepcopy
    copied = [num for num in array]
    # this list is to store the value when popping the min in removeMin
    some = []
    buildMinHeap(array)
    printMinHeap(array, some)
    # only prints if the sorted original copied list is the same as the list that was being inserted to by printMinHeap
    if some == sorted(copied):    
        print('SUCCESS')


if __name__ == "__main__":
	main()