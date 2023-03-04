# COUNTING SORT

# importing necessary utilitites
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
import time
import numpy as np


def counting_sort(array, output, max):
    '''
sorts the given array using counting sort
'''

	# count array to store count of each element
    # the size of the max element given
    count = [0 for i in range(max)]

	# storing count of each element
    for i in array:
        count[i] += 1

	# making it a cumulative frequency list
    # now it has positions of each element
    for i in range(1, max):
        count[i] += count[i-1]

	# Build the output character array
    for i in range(len(array)-1, -1, -1):
        output[count[array[i]]-1] = array[i]
        count[array[i]] -= 1
    
    return output


def main():
    '''
tests the counting_sort() & measures its
time complexity on different input sized iterables
'''

    # maximum size of varying sized iterable
    SIZE = 50000

    # Dataframe containing time used & size of iterable
    data = dict()
    data['time'] = list()
    data['size'] = list()

    # headers for displayed output
    print('Counting Sort:\n')
    print('size\ttime')

    # maximum element possible in iterable
    list_max = 100

    # for different input sized iterables
    for list_size in range(10, SIZE, 25):

        # populating the input & output array
        array = list(np.random.randint(low=list_max, size=list_size))
        output = [0 for i in range(list_size)]

        # recording the time used
        start = time.time()
        array = counting_sort(array, output, list_max)
        end = time.time()

        # dispalying results
        print(f'{list_size}\t{end-start}')

        # populating dataframe
        data['time'].append(end-start)
        data['size'].append(list_size)

        # updating max element possible
        # list_max += 200

    # creating & plotting dataframe
    df = pd.DataFrame(data, columns=['time', 'size'])
    df.plot(x='size', y='time', kind='scatter')

    # displaying scatter plot
    plt.show()

if __name__ == '__main__':
    main()
