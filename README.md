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

        Building a Binary Heap: O(n)
        Heapify:                O(lgn)

        Total RunTime:          O(nlgn)

Some Properties:
    iParent(i)     = floor((i-1) / 2) where floor functions map a real number to the smallest leading integer.
    iLeftChild(i)  = 2*i + 1
    iRightChild(i) = 2*i + 2