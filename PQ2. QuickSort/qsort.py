

###===================================================================
### Count the number of cmparisions in quick sort algorithm.

def count_cmp_quick_sort(array, low, high, pivot_fn):
    if low >= high: return 0
    pivot = pivot_fn(array, low, high)

    # index of pivot in final sorted array
    idx = partition(array, low, high, pivot)

    count_left = count_cmp_quick_sort(array, low, idx - 1, pivot_fn)
    count_right = count_cmp_quick_sort(array, idx + 1, high, pivot_fn)
    return count_left + count_right + (high - low)

def partition(array, low, high, pivot):
    """ Partition the array around the first element(pivot) so that all
    elements less than pivot are to the left of it, while all greater
    elements are to its right.
    

    We do partition by maintain the following invariant:
    
    -----------------------------------
    |p|    < p  |   >p   |      ?     |
    -----------------------------------
    low         i        j            high

    and then swap pivot to its right position(e.g. i-1):

    -----------------------------------
    |   < p         |p|      > p      |
    -----------------------------------
    low               i               j
                                      high

    """
    assert pivot == array[low], "pivot must be the first element."
    i = low + 1
    for j in range(low + 1, high + 1):
        if array[j] < pivot:
            swap(array, i, j)
            i += 1
    swap(array, low, i - 1)
    return i - 1

###===================================================================
### Different function for choose pivot, and exchange the pivot element
### (i.e., the last element) with the first element.

def first_ele(array, low, high):
    return array[low]

def last_ele(array, low, high):
    swap(array, low, high)
    return first_ele(array, low, high)

def median_ele(array, low, high):
    idx = median_idx(array, low, high)
    swap(array, low, idx)
    return first_ele(array, low, high)

def median_idx(array, low, high):
    """ Return median index of three indexs(low, high, middle).

    e.g:
    >>> median_idx([5, 4, 6], 0, 2)
    0
    """
    middle = (high - low) / 2 + low
    idxs = [low, high, middle]
    return sorted(map(lambda x: [array[x], x], idxs))[1][1]

###===================================================================
### Util functions

def create_array(filename):
    array = []
    f = open(filename, 'r')
    for line in f:
        array.append(int(line))
    f.close()
    return array

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
    
def run(array, pivot_fn):
    return count_cmp_quick_sort(array, 0, len(array)-1, pivot_fn)


###===================================================================
### main test

if __name__ == '__main__':
    import sys

    fpath = sys.argv[1]
    f = open(fpath, 'r')
    lines = f.readlines()
    f.close()
    lines = [int(line) for line in lines]
    print lines

    a = lines
    sorted_a = sorted(a)
    for fn in [first_ele, last_ele, median_ele]:
        b = a[:]
        print fn.func_name, run(b, fn)
        assert b == sorted_a
    
