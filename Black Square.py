n = list(map(int, input().split()))
s = input()
cal = 0
for i in range(len(s)):
    int_s = int(s[i])
    cal += n[int_s - 1]

print(cal)
