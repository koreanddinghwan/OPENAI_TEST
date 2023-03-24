# 1. Take input
n, a, b = map(int, input().split())
tasks = list(map(int, input().split()))

# 2. Calculate min_A and max_B
sorted_tasks = sorted(tasks)
min_A = sorted_tasks[n-a]
max_B = sorted_tasks[b-1]
A_tasks = sorted_tasks[-a:]
B_tasks = sorted_tasks[:-a]

# 3. Iterate over all possible x and count valid values
count = 0
for x in range(max_B+1, min_A):
    assigned_to_A = [task for task in A_tasks if task > x]
    assigned_to_B = [task for task in B_tasks if task < x]
    if len(assigned_to_A) == a and len(assigned_to_B) == b:
        count += 1

# 4. Print output
print(count)
