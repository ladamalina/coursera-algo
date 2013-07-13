import sys

fpath = sys.argv[1]
f = open(fpath, 'r')
lines = f.readlines()
f.close()
lines = [int(line) for line in lines]

# for tests
# lines = sys.argv[1].split(' ')
# lines = [int(line.strip(',')) for line in lines]

def invCount(arr):
    if len(arr) < 2:
        return 0
    m = int ((len(arr) + 1) / 2)
    left = arr[0:m]
    right = arr[m:]
    return invCount(left) + invCount(right) + merge(arr, left, right);
    
def merge(arr, left, right):
    i, j, count = 0,0,0
    while i < len(left) or j < len(right) :
        if i == len(left):
            arr[i+j] = right[j]
            j+=1
        elif j == len(right) :
            arr[i+j] = left[i]
            i+=1
        elif left[i] <= right[j] :
            arr[i+j] = left[i]
            i+=1              
        else:
            arr[i+j] = right[j]
            count += len(left)-i
            j+=1
    return count

print invCount(lines)
