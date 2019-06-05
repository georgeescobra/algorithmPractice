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
