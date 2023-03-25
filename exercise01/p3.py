# Process each test case and return a list of drenched layers
def process_test_case(n, a):
    drenched = [0] * n
    for i in range(n):
        x = a[i]
        if x == 0:
            continue
        elif x >= i+1:
            drenched[0:i+1] = [1] * (i+1)
        else:
            for j in range(x):
                drenched[i-j] = 1
    return drenched


# Read the number of test cases
t = int(input())

# Process each test case and store the results in a list
results = []
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    result = process_test_case(n, a)
    results.append(result)

# Print the results
for result in results:
    print(*result)
