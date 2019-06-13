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

def removeElement(list):
	#print(list)
	temp = list[0]
	del list[0]
	minHeapify(list, 0)
	#print(list)
	return temp

def buildMinHeap(list):
	# range(start, stop, step)
    for position in range(len(list) // 2, -1, -1):
        minHeapify(list, position)

def printMinHeap(list):
	#while list:
		#print(removeElement(list
	for i in range(50):
		print(removeElement(list))

def main():
	array = [random.randint(0, 100) for i in range(50)]
	# one way to do it without having to use deepcopy
	copied = [num for num in array]
	buildMinHeap(array)
	#print(array)
	printMinHeap(array)



if __name__ == "__main__":
	main()