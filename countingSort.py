def countingSort(arr):
    result=[0]*100
    for j in range(len(arr)):
        result[arr[j]]+=1
    return result
