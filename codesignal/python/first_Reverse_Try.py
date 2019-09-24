def firstReverseTry(arr):
    if (len(arr)>1) : arr[0],arr[len(arr)-1] = arr[len(arr)-1],arr[0]
    return arr
