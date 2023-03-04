# MERGE SORT

# importing necessary utilitites
import pandas as pd
import matplotlib.pyplot as plt
import time
import numpy as np


def merge_sort(array):
	'''
sorts the given array by using merge sort
'''
    
    # until array is a single element
	if len(array) > 1:

		# Finding the mid of the array
		mid = len(array)//2

		# Dividing the array elements into 2 lists
		left = array[:mid]
		right = array[mid:]

		# Sorting the both halves
		merge_sort(left)
		merge_sort(right)

		i = j = k = 0

		# merging both sorted arrays into one
		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				array[k] = left[i]
				i += 1
			else:
				array[k] = right[j]
				j += 1
			k += 1

		# if left list is not empty yet
		while i < len(left):
			array[k] = left[i]
			i += 1
			k += 1

        # if right list is not empty yet
		while j < len(right):
			array[k] = right[j]
			j += 1
			k += 1


def main():
    '''
tests the merge_sort() & measures its
time complexity on different input sized iterables
'''

    # maximum size  of varying sized iterable
    SIZE = 50000

    # Dataframe containing time used & size of iterable
    data = dict()
    data['time'] = list()
    data['size'] = list()

    # headers for displayed output
    print('Merge Sort:\n')
    print('size\ttime')

    # for different input sized iterables
    for list_size in range(10, SIZE, 25):

        # populating the array
        array = list(np.random.randint(low=100, size=list_size))

        # recording the time used
        start = time.time()
        merge_sort(array)
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
