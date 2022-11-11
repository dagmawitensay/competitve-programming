
def countSwaps(a):
    swaps=0
    for i in range(n):
        for j in range(n-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                swaps+=1
        if swaps==0:
            break
    print(f"Array is sorted in {swaps} swaps")
    print(f"First element: {a[0]}")
    print(f"Last element : {a[len(a)-1]}")

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
