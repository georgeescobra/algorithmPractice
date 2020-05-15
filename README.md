THINGS LEARNED ABOUT SELECTION SORT

  Selection Sort is an algorithm that is based on the idea of finding the minimum or
  maximum element in an unsorted array and then putting it in its correct position
  in a sorted array.

  This means that the iterator will start at index 1 and this will be either the minimum
  or maximum--depending on whether the array is going to be ascending or descending--and
  this will be compared to to the rest of the array finding another element that is either
  smaller or bigger than it.

  Once the iterator has gone through the whole array, the program will then swap whatever
  element is in the minimum or maximum place holder to the index, and this process
  repeats until the whole list is sorted.

Time Complexities:
  Best:     Ω(n^2)
  Average:  Θ(n^2)
  Worst:    O(n^2)

  As shown above, the time complexity of selection sort is very inefficient as the
  algorithm has to constantly compare each element with the rest of the array, going
  through the array n^2 time.

Simple Walk-Through of Selection Sort(ascending):

    Array = [9, 6, 4, 3, 1, 7]

    1st Iteration:
      index = 0
      Minimum = 9
      9 < 6 False
      Minimum = 6
      6 < 4 False
      Minimum = 4
      4 < 3 False
      Minimum = 3
      3 < 1 False
      Minimum = 1
      1 < 7 True
      Array[index] = Minimum
      [1, 9, 6, 4, 3, 7]

    2nd Iteration:
      index = 1
      Minimum = 9
      9 < 6 False
      Minimum = 6
      6 < 4 False
      Minimum = 4
      4 < 3 False
      Minimum = 3
      3 < 7 True
      Array[index] = Minimum
      [1, 3, 9, 6, 4, 7]

    3rd Iteration:
      index = 2
      Minimum = 9
      9 < 6 False
      Minimum = 6
      6 < 4 False
      Minimum = 4
      4 < 7 True
      Array[index] = Minimum
      [1, 3, 4, 9, 6, 7]

    4th Iteration:
      index = 3
      Minimum = 9
      9 < 6 False
      Minimum = 6
      6< 7 True
      Array[index] = Minimum
      [1, 3, 4, 6, 9, 7]

    5th Iteration:
      index = 4
      Minimum = 9
      9 < 7 False
      Minimum = 7
      Array[index] = Minimum
      [1, 3, 4, 6, 7, 9]


THINGS LEARNED ABOUT QUICK SORT

	*interesting to note: in the unit_test when I tried to input 100,000 elements, it returned an error
	due to RecursionError: maximum recursion depth exceeded in comparison"*

	Quick Sort is a recursive algorithm that uses divide and conquer
	Quick Sort does not use additional storage like merge sort does
	Pretty Practical Algorithm

	Time Complexities:
		Best:		Ω(n lg n)
		Average:	Θ(n lg n)
		Worst:		O(n^2)

	You can improve your chances of getting an average running time by choosing different pivot positions
	Quick Sort's best case occurs when the partitions are as even as possible, meaning the sizes are equal or within 1 of each other
	However when this doesn't happen often (although you are able to increase your chances)
	If you get a partition that is a 3 to 1 split (3n/4 and n/4 split)
		If the pivot is chosen in the middle half, there is a 50% chance the split is at worse a 3 to 1 split

	"In fact, with a little more effort, you can improve your chance of getting a split that's at worst 3-to-1. Randomly choose not one, but three elements from the subarray, and take median of the three as the pivot (swapping it with the rightmost element). By the median, we mean the element of the three whose value is in the middle. We won't show why, but if you choose the median of three randomly chosen elements as the pivot, you have a 68.75% chance (11/16) of getting a 3-to-1 split or better. You can go even further. If you choose five elements at random and take the median as the pivot, your chance of at worst a 3-to-1 split improves to about 79.3% (203/256). If you take the median of seven randomly chosen elements, it goes up to about 85.9% (1759/2048). Median of nine? About 90.2% (59123/65536). Median of 11? About 93.1% (488293/524288). You get the picture. Of course, it doesn't necessarily pay to choose a large number of elements at random and take their median, for the time spent doing so could counteract the benefit of getting good splits almost all the time."
		https://www.khanacademy.org/computing/computer-science/algorithms/quick-sort/a/analysis-of-quicksort
		***see link for a walk through***


THINGS LEARNED ABOUT MERGESORT

Merge sort is a recursive algorithm that continuously splits a list in half
It will start to sort once the splits have reached a size of one
Once the two halves are sorted then they are merged

Note: The lists when sliced may not be evenly cut in half, but does not matter because 
	  the lengths will differ by at most one

Runtime Analysis:
	Merging runs Θ(n)
	MergeSort runs Θ(n lg n)
https://www.khanacademy.org/computing/computer-science/algorithms/merge-sort/a/analysis-of-merge-sort

Walk-Through:
	https://medium.com/@amirziai/merge-sort-walkthrough-with-code-in-python-e4f76d90a4ea


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
    

Everything Learned About HeapSort

Heaps have rules:
    It is a binary tree
    It is filled from left to right
    Can either be ordered as Max Heap or Min Heap
        Every Parent Node is either greater than or equal to the value of its children nodes(max Heap)
        Every Parent Node is either less than or equal to the value of its children nodes(min Heap)
    First we BuildMinHeap() (in the program i created it is a min heap)
    The Root Node will always contain the minimum value or max value depending on type of heap
    In order to get the ascending order of heap you store the root value and replace the root value with the last element of the list
    After this you then have to call heapify since the heap no longer satisfies the heap properties

    WalkThrough: 
        https://medium.com/basecs/heapify-all-the-things-with-heap-sort-55ee1c93af82

THINGS LEARNED ABOUT BINARY SEARCH TREE

    -Left Subtree cotains values less than the root
    -Right Subtree contains values greater than the root
    -left and right subtrees must also be binary search trees
    -Duplicates are not allowed
        --by definition the left and right nodes but be smaller and greater respectively
        --can be implemented tho, by using the right node as <= 
    -Full Binary Tree
        -each node in the tree has exactly 2 children or 0 children
    -Complete Binary Tree
        -a binary tree is completely filled with the exception of the bottom level
    -height h of a complete binary binary tree with N nodes is at most O(log N)
    -Trees provide an efficient insertion and search
    -Trees are flexible, allowing to move subtrees with minimum effort
    
   

        Building a Binary Heap: O(n)
        Heapify:                O(lgn)

        Total RunTime:          O(nlgn)


Some Properties:
    iParent(i)     = floor((i-1) / 2) where floor functions map a real number to the smallest leading integer.
    iLeftChild(i)  = 2*i + 1
    iRightChild(i) = 2*i + 2


Each branch will contain a README that contains notes on each of the algorithms.
ALGORITHM BRANCHES:
  1. insertion_sort
  2. selection_sort
  3. quick_sort
  4. merge_sort
  5. heap_sort
  6. binary_search_tree
  7. breadth_first_search

