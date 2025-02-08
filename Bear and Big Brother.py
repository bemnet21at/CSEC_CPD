a,b = map(int, input().split())
year = 0

while (b >= a):
    a = a * 3
    b = b * 2
    year = year + 1
print(year)
