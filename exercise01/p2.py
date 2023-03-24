# 1. Input phase
n = int(input())
houses = list(map(int, input().split()))

# 2. Check phase
houses.sort()  # Sort the list of houses
can_commit_crime = False

# Iterate over all possible combinations of three houses
for i in range(n - 2):
    if houses[i] != houses[i+1] and houses[i] != houses[i+2] and houses[i+1] != houses[i+2]:
        if abs(houses[i] - houses[i+1]) <= 2 and abs(houses[i+1] - houses[i+2]) <= 2 and abs(houses[i] - houses[i+2]) <= 2:
            can_commit_crime = True
            break

# 3. Output phase
if can_commit_crime:
    print("YES")
else:
    print("NO")
