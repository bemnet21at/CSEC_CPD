n = int(input())
action = list(map(int, input().split()))

p = 0
c = 0

for i in range(n):
    if action[i] < 0:
        if p > 0:
            p += action[i]
            if p < 0:
                c += abs(p)
                p = 0
        else:
            c += abs(action[i])
    else:
        p += action[i]

print(c)
