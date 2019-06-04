THINGS LEARNED ABOUT INSERTION SORT
# 	O(n^2) (quadratic running time)
	Does not bode well for large inputs because as input doubles, the time it takes to sort
	will be quadruple
#	The best case scenario for insertion sort is O(n) when everything is sorted
	This is because less comparisons are needed to be made by inner loop

#	Space complexity is in-place

#	Insertion Sort maintains two sublists
	a sorted sublist, and an unsorted sublist

#	The left side is sorted and right side is unsorted


# 	Assumes the first element of the list is sorted and starts
	at the second element and inserts into sublist sorted

#	Simple walk through of Insertion Sort(ascending):
    Array = [9, 7, 6, 3, 4, 5]
    1st Iteration:
        i = 1
        Starts at the second element and works backwards
        9 > 7 True
        i = 0
        [7, 9, 6, 3, 4, 5]
    2nd Iteration:
        i = 2
        9 > 6 True
        i = 1
        7 > 6 True
        i = 0
        [6, 7, 9, 3, 4, 5]
    3rd Iteration:
        i = 3
        9 > 3 True
        i = 2
        7 > 3 True
        i = 1
        6 > 3 True
        i = 0
        [3, 6, 7, 9, 4, 5]
    4th Iteration:
        i = 4
        9 > 4 True
        i = 3
        7 > 3 True
        i = 2
        6 > 4 True
        i = 1
        3 > 4 False
        [3, 4, 6, 7, 9, 5]
    5th Iteration:
        i = 5
        9 > 5 True
        i = 4
        7 > 5 True
        i = 3
        6 > 5 True
        i = 2
        4 > 5 False
        [3, 4, 5, 6, 7, 9]
    

