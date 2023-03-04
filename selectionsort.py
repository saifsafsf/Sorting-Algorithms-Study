# SELECTION SORT

# importing necessary utilitites
import pandas as pd
import matplotlib.pyplot as plt
import time
import numpy as np


def selection_sort(array, size):
    '''
takes a iterable & number of elements in it
returns the iterable sorted using selection sort
'''
    
    # index1 going through the iterable
    for index1 in range(0, size-1):
        
        # assumed minimum index
        minim = index1

        # locating minimum from the right part of minim
        for index2 in range(index1+1, size):
            if array[index2] < array[minim]:
                minim = index2

        if minim != index1:
            array[index1], array[minim] = array[minim], array[index1]

def main():
    '''
tests the selection_sort() & measures its
time complexity on different input sized iterables
'''

    # maximum size of varying sized iterable
    SIZE = 10000

    # Dataframe containing time used & size of iterable
    data = dict()
    data['time'] = list()
    data['size'] = list()

    # headers for displayed output
    print('Selection Sort:\n')
    print('size\ttime')

    # for different input sized iterables
    for list_size in range(10, SIZE, 25):

        # populating the array
        array = list(np.random.randint(low=100, size=list_size))

        # recording the time used
        start = time.time()
        selection_sort(array, list_size)
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
