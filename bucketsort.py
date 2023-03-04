# BUCKET SORT

# importing necessary utilitites
import pandas as pd
import matplotlib.pyplot as plt
import time
import numpy as np


def insertion_sort(array, size):
    '''
takes a iterable & number of elements in it
returns the iterable sorted using insertion sort
'''
    
    # index1 going through the iterable
    for index1 in range(1, size):
        
        # current element
        key = array[index1]
        index2 = index1 - 1

        # index2 placing key behind index1 in its right place
        while index2 >= 0 and array[index2] > key:

            # smaller key moving to the start of iterable
            array[index2+1] = array[index2]
            index2 -= 1

        # updating the final element
        array[index2+1] = key	
			

def bucket_sort(array):
    '''sorts the given iterable using bucket sort
'''
    
    # array to store buckets & num of buckets
    buckets = []
    slot_num = 10
    
    # initializing the lists in each bucket
    for i in range(slot_num):
        buckets.append([])
		
	# putting elements in corresponding buckets
    for j in array:
        buckets[int(slot_num * j)].append(j)
	
	# sorting each buckets
    for i in range(slot_num):
        insertion_sort(buckets[i], len(buckets[i]))

    # to store output now
    array.clear()
		
	# concatenating the sorted buckets
    for i in range(len(buckets)):
        array += buckets[i]


def main():
    '''
tests the bucket_sort() & measures its
time complexity on different input sized iterables
'''

    # maximum size of varying sized iterable
    SIZE = 20000

    # Dataframe containing time used & size of iterable
    data = dict()
    data['time'] = list()
    data['size'] = list()

    # headers for displayed output
    print('Bucket Sort:\n')
    print('size\ttime')

    # for different input sized iterables
    for list_size in range(10, SIZE, 25):

        # populating the array
        array = list(np.random.uniform(size=list_size))

        # recording the time used
        start = time.time()
        bucket_sort(array)
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
