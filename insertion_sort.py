def insertionSort1(n,arr):
    for i in range(n-1,-1,-1):
        key=arr[i]
        j=i
        while j>0 and arr[j-1]>key:
            arr[j]=arr[j-1]
            j-=1
            print(" ".join(map(str,arr)))
        arr[j]=key
    print(" ".join(map(str,arr)))

    