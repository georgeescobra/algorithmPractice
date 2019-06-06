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




















