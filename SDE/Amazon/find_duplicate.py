def printRepeating(arr, size):
 
    print("The repeating elements are: ")
 
    for i in range(0, size):
 
        if arr[abs(arr[i])] >= 0:
            arr[abs(arr[i])] = -arr[abs(arr[i])]
        else:
            print(abs(arr[i]), end=" ")
