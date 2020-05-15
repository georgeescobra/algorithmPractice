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
