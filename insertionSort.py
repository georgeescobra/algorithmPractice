import random   #   module used to generate random numbers for the list
import copy     #   module used to deep copy original list

#   if i did not use deep copy then and simply just did something like copy = origList
#   the origList will be changed as i change the copied list since it is only a shallow deepcopy
#   meaning that the copiedList elements points to the relative origList's elements' mem address
#   deepcopy makes it so that the copied list has its own set of objects rather than just pointing
#   to the origList elements

randomList = []
for i in  range(50):
    randomList.append(random.randrange(1, 100, 1))

orderedList = copy.deepcopy(randomList)
for index in range(1, len(orderedList)):
    currentValue = orderedList[index]
    position = index
    #   If i want it to be descending order just flip condition to orderedList[position -  1] < currentValue
    while position > 0 and orderedList[position - 1] > currentValue:
        orderedList[position] = orderedList[position - 1]
        position = position - 1

    orderedList[position] = currentValue

print('Sorting List of 50 Elements in Ascending Order')

#   One way to format a string in python3
#   '0' in 0:5 refers to the index of the arguments being passed in format()
print('{0:5} ==> {1:5}'.format('Original','Sorted'))

#   Best way to go through two lists at the same time using zip

for orig, sorted in zip(randomList, orderedList):
    print('{0:5}    ==>  {1:5d}'.format(orig, sorted))
