# Python Program to implement Bubble Sort Algorithm.


def bubbleSort(arr):
	array_length = len(arr)

	# Traversing through all array elements
	for i in range(array_length):
		for j in range(0, array_length-i-1):

			# Compare elemnts and swap if element found is greater
			# than next element
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]

	return arr




if __name__ == "__main__":
	arr = [8,5,3,1,4,7,9]

	sorted_arr = bubbleSort(arr)

	print("Sorted Array is: ")
	print(sorted_arr)