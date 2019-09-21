def adjacentElementsProduct(inputArray):
    m = -1001
    for i in range(len(inputArray)-1):
        if ((inputArray[i]*inputArray[i+1]) > m):
            m = (inputArray[i]*inputArray[i+1]) 
    return m
