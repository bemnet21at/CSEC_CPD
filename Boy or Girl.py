name = input()
name_list = []

for i in range(len(name)):
    if name[i] not in name_list:
        name_list.append(name[i])
char = len(name_list)
if char % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
