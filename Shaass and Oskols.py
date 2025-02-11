n = int(input())
a = list(map(int, input().split()))
m = int(input())
for _ in range(m):
    x = list(map(int, input().split()))
    if (x[0] - 1) > 0:
        a[x[0] - 2] += x[1] - 1
    
    if x[0] - 1 < n - 1:
        a[x[0]] += a[x[0]-1]-x[1]
        
    a[x[0]-1] = 0

for i in range(len(a)):
    print(a[i])
