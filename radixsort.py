# RADIX SORT

# importing necessary utilitites
import math
import pandas as pd
import matplotlib.pyplot as plt
import time
import numpy as np


def counting_sort(array, size, d):
    '''
sorts the given iterable using counting sort
but on the basis of dth digit
'''
    
    # initializing array to store sorted elements
    output = [0] * size

	# count array to store count of each element
    # the size of the max element given
    count = [0 for i in range(10)]

	# storing count of each element
    for i in array:
        count[(i//d) % 10] += 1

	# making it a cumulative frequency list
    # now it has positions of each element
    for i in range(1, 10):
        count[i] += count[i-1]

	# Build the output character array
    for i in range(len(array)-1, -1, -1):
        output[count[(array[i]//d) % 10]-1] = array[i]
        count[(array[i]//d) % 10] -= 1

    return output


def radix_sort(array, size, d):
    '''
sorts the given iterable using radix sort
d is the max number of digits
'''

    # sorting by ith integer in each pass
    i = 1
    
    while i < math.pow(10, d):

        # counting sort on ith integer's basis
        array = counting_sort(array, size, i)
        i *= 10

    return array

def main():
    '''
tests the radix_sort() & measures its
time complexity on different input sized iterables
'''

    # maximum size of varying sized iterable
    SIZE = 25000

    # Dataframe containing time used & size of iterable
    data = dict()
    data['time'] = list()
    data['size'] = list()

    # headers for displayed output
    print('Radix Sort:\n')
    print('size\ttime')

    d = 3

    # for different input sized iterables
    for list_size in range(10, SIZE, 25):

        # populating the input array
        array = list(np.random.randint(low=math.pow(10, d), size=list_size))

        # recording the time used
        start = time.time()
        array = radix_sort(array, len(array), d)
        end = time.time()

        # dispalying results
        print(f'{list_size}\t{end-start}')

        # populating dataframe
        data['time'].append(end-start)
        data['size'].append(list_size)

        d += 0.006

    # creating & plotting dataframe
    df = pd.DataFrame(data, columns=['time', 'size'])
    df.plot(x='size', y='time', kind='scatter')

    # displaying scatter plot
    plt.show()

if __name__ == '__main__':
    main()
