
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    prefs = [0] * (n)
    max_val = float('-inf')
    pref_sum = 0
    
    for a, b, k in queries:
        prefs[a - 1] += k
        if b < n:
            prefs[b] -= k
    
    for i in range(len(prefs)):
        pref_sum += prefs[i]
        max_val = max(max_val, pref_sum)

    return max_val

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')
