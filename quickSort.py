#	this version of quicksort will use the last element of the array as a pivot
import random
import copy

def quickSort(array, low, high):
	if(low < high):
		partitionIndex = partition(array, low, high)
		quickSort(array, low, partitionIndex - 1)
		quickSort(array, partitionIndex + 1, high)
	#	don't necessarily have to return, but doing so for the sake of the unit_test
	return array


def partition(array, low, high):
	index = low - 1
	pivot = array[high]

	for j in range(low, high):
		if array[j] <= pivot:
			index += 1
			#	this swaps the values of array[i] and array[j]
			array[index], array[j] = array[j], array[index]
	array[index + 1], array[high] = array[high], array[index + 1]
	return index + 1


def main():
	unordered = [random.randint(0, 100) for i in range(50)]

	orig = copy.deepcopy(unordered)

	quickSort(unordered, 0, len(unordered) - 1)
	print('Sorting List of 50 Elements in Ascending Order')

	print('{0:5} ==> {1:5}'.format('Original','Sorted'))

	for orig, sorted in zip(orig, unordered):
	    print('{0:5}    ==>  {1:5d}'.format(orig, sorted))


#	this is the proper way of having a 'main' function in python3
#	this is important for the purpose of code reusability and if this module is imported
#	this means that gives the ability to conditionally execute the main function is important when writing code that could be possibly used by others

if __name__ == "__main__":
	main()