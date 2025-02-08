n = int(input())
stones = input()
count = 0
for i in range(n):
    if i < n-1 and stones[i] == stones[i+1]:
        count += 1
print(count)
