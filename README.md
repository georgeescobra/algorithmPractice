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