shoe = list(map(int, input().split()))
new_shoe = []
count = 0
for i in range(4):
    if shoe[i] in new_shoe:
        count += 1
    else:
        new_shoe.append(shoe[i])
print(count)
