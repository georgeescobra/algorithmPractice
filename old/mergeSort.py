import random
import copy

def mergeSort(sorting):
	if len(sorting) > 1:
		midPoint = len(sorting)//2
		# this is called splycing
		leftHalf = sorting[:midPoint]	# from 0 to midPoint - 1 (excluding)
		rightHalf = sorting[midPoint:]	# from midPoint to end of list

		mergeSort(leftHalf)
		mergeSort(rightHalf)

		i = 0
		j = 0
		k = 0
		while i < len(leftHalf) and j < len(rightHalf):
			if leftHalf[i] < rightHalf[j]:
				sorting[k] = leftHalf[i]
				i += 1
			else:
				sorting[k] = rightHalf[j]
				j += 1
			k += 1

		while i < len(leftHalf):
			sorting[k] = leftHalf[i]
			i += 1
			k += 1

		while j < len(rightHalf):
			sorting[k] = rightHalf[j]
			j += 1
			k += 1


# produces a list of random ints with 50 elements
array = [random.randint(0, 100) for i in range(50)]

copied = copy.deepcopy(array)

mergeSort(array)

print('Sorting List of 50 Elements in Ascending Order')

print('{0:5} ==> {1:5}'.format('Original','Sorted'))

for orig, sorted in zip(copied, array):
    print('{0:5}    ==>  {1:5d}'.format(orig, sorted))