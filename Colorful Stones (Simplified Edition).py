s = input()
t = input()
i = 0
pos = 1
for j in range(len(t)):
    if s[i] == t[j]:
        pos += 1
        i += 1
print(pos)
