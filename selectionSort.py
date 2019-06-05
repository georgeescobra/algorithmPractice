import random
import copy

#   this is the array that is going to get ordered by Selection Sort
#   this is a one liner, filling an array with 50 elements of random ints between
#   0 and 100
array = [random.randint(0, 100) for i  in range(50)]

#   this is too keep track of the original set of numbers to compare
orig = copy.deepcopy(array)

#   Sorting the Array
for i in range(len(array)):
    #   minimum needs to be initialized as a place holder
    minimumPos = i
    for j in range(i+1, len(array)):
        #   This will sort in ascending order, if i want it to be descending just
        #   flip the condition to 'array[j] > array[minimumPos]'
        if array[j] < array[minimumPos]:
            minimumPos = j

    #   Swaps at the end of each outter for loop iteration
    #   Remember this way in order to swap elements
    array[i], array[minimumPos] = array[minimumPos], array[i]

#   this is a check to see if the list was sorted properly
#   sorted is a built-in python function to sort the list in ascending order
#   if you want descending order add 'reverse = True' as a parameter in the sorted
#   function call

#   function to make sure that the array was sorted properly
#   sorted() returns a new list so no need to worry about it changing original list
success = True
for check, sorted in  zip(sorted(orig), array):
    if check != sorted:
        success = False

if success:
    print('Sorting List of 50 Elements in Ascending Order')

    print('{0:5} ---> {1:5}'.format('Original', 'Sorted'))

    for original, sorted in zip(orig, array):
        print('{0:5} {2} {1:5d}'.format(original, sorted, '  ---->'))

else:
    print('FAILED')
