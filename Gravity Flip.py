n = int(input())
cubes = list(map(int, input().split()))
i = 0

for i in range(n):
    for j in range(n - i - 1):
        if i + 1 < len(cubes) and cubes[j] > cubes[j + 1]:
            temp = cubes[j]
            cubes[j] = cubes[j+1]
            cubes[j+1] = temp
for k in range(n):
    print(cubes[k], end=" ")

