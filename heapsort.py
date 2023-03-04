# HEAP SORT

# importing necessary utilitites
import pandas as pd
import matplotlib.pyplot as plt
import time
import numpy as np


def heapify(arr, n, i):
	'''
heapifies the given root 
'''
    
    # assuming root is largest
	largest = i

    # left & right child
	left = 2*i + 1
	right = 2*i + 2

	# if left child of root exists & is greater than root
	if left < n and arr[largest] < arr[left]:
		largest = left

	# if right child of root exists & is greater than root
	if right < n and arr[largest] < arr[right]:
		largest = right

	# updating root, if changed, swapping with parent
	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i]

		# heapifying the swapped root
		heapify(arr, n, largest)


def heap_sort(array):
	'''
sorts the given iterable using heap sort
'''
	n = len(array)

	# building a maxheap
	for i in range(n//2 - 1, -1, -1):
		heapify(array, n, i)

	# placing maximums at the end, heapifying remaining
	for i in range(n-1, 0, -1):
		array[i], array[0] = array[0], array[i]
		heapify(array, i, 0)


def main():
    '''
tests the heap_sort() & measures its
time complexity on different input sized iterables
'''

    # maximum size of varying sized iterable
    SIZE = 50000

    # Dataframe containing time used & size of iterable
    data = dict()
    data['time'] = list()
    data['size'] = list()

    # headers for displayed output
    print('Heap Sort:\n')
    print('size\ttime')

    # for different input sized iterables
    for list_size in range(10, SIZE, 25):

        # populating the array
        array = list(np.random.randint(low=100, size=list_size))

        # recording the time used
        start = time.time()
        heap_sort(array)
        end = time.time()

        # dispalying results
        print(f'{list_size}\t{end-start}')

        # populating dataframe
        data['time'].append(end-start)
        data['size'].append(list_size)

    # creating & plotting dataframe
    df = pd.DataFrame(data, columns=['time', 'size'])
    df.plot(x='size', y='time', kind='scatter')

    # displaying scatter plot
    plt.show()

if __name__ == '__main__':
    main()
