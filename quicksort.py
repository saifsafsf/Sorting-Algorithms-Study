# QUICK SORT

# importing necessary utilitites
import pandas as pd
import matplotlib.pyplot as plt
import time
import numpy as np


def median(array, start, mid, end):
    '''
returns the median index of given list & three indices
'''

    if array[start] > array[mid]:
        if array[start] < array[end]:
            median = start

        elif array[mid] > array[end]:
            median = mid

        else:
            median = end

    else:
        if array[start] > array[end]:
            median = start

        elif array[mid] < array[end]:
            median = mid

        else:
            median = end

    # returning index of median found
    return median


def partition(array, start, end):
    '''
takes an array, start & end index
returns an index with smaller elements on one side
while greater on the other side
'''

    # finding median & placing it in the end
    med = median(array, start, (start+end)//2, end)
    array[end], array[med] = array[med], array[end]

    # choose the rightmost element as pivot
    pivot = array[end]

    # pointer for greater element
    i = start - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(start, end):
        if array[j] <= pivot:
            # if element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # swapping element at i with element at j
            array[i], array[j] = array[j], array[i]

    # swap the pivot element with the greater element specified by i
    array[i + 1], array[end] = array[end], array[i + 1]

    # return the position from where partition is done
    return i + 1


def quick_sort(array, start, end):
    '''
takes a iterable, start & end index
returns the iterable sorted using quick sort
'''

    # start has not crossed end index
    if start < end:

        # the dividing point
        point = partition(array, start, end)

        # sorting the resulting 2 arrays
        quick_sort(array, start, point-1)
        quick_sort(array, point+1, end)


def main():
    '''
tests the quick_sort() & measures its
time complexity on different input sized iterables
'''

    # maximum size of varying sized iterable
    SIZE = 50000

    # Dataframe containing time used & size of iterable
    data = dict()
    data['time'] = list()
    data['size'] = list()

    # headers for displayed output
    print('Quick Sort:\n')
    print('size\ttime')

    # for different input sized iterables
    for list_size in range(10, SIZE, 25):

        # populating the array
        array = list(np.random.randint(low=100, size=list_size))

        # recording the time used
        start = time.time()
        quick_sort(array, 0, list_size-1)
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
