# BUBBLE SORT

# importing necessary utilitites
import pandas as pd
import matplotlib.pyplot as plt
import time
import numpy as np


def bubble_sort_enhanced(array, size):
    '''
takes a iterable & number of elements in it
returns the iterable sorted using enhanced bubble sort
'''

    # index1 going through the iterable
    for index1 in range(0, size-1):

        # flag var to check if iterable is sorted
        swap = 0
        
        # index2 going through the iterable in the left part of index1
        for index2 in range(0, size-index1-1):

            # if 2 unordered elements found, swap them
            if array[index2] > array[index2+1]:
                array[index2], array[index2+1] = array[index2+1], array[index2]
                swap += 1

        # if flag remains unchanged, iterable is sorted
        if swap == 0:
            break


def main():
    '''
tests the bubble_sort_enhanced() & measures its
time complexity on different input sized iterables
'''

    # maximum size of varying sized iterable
    SIZE = 10000

    # Dataframe containing time used & size of iterable
    data = dict()
    data['time'] = list()
    data['size'] = list()

    # headers for displayed output
    print('Bubble Sort:\n')
    print('size\ttime')

    # for different input sized iterables
    for list_size in range(10, SIZE, 25):

        # populating the array
        array = list(np.random.randint(low=100, size=list_size))

        # recording the time used
        start = time.time()
        bubble_sort_enhanced(array, list_size)
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
