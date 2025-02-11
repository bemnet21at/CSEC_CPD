a = list(map(int, input().split()))
largest = max(a[0], a[1])
dies = [1,2,3,4,5,6]
count = 0
for i in range(6):
    if dies[i] >= largest:
        count += 1
if count % 2 == 0 and count % 6 != 0:
    print(f"{int(count/2)}/3")
elif count % 3 == 0 and count % 6 != 0:
    print(f"{int(count/3)}/2")
elif count % 6 == 0:
    print("1/1")
else:
    print(f"{count}/6")
