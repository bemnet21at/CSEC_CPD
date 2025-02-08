n = int(input())
count_one = 0
count_game = 0
for _ in range(n):
    game = list(input().split())
    for i in range(len(game)):
        if game[i] == '1':
            count_one = count_one + 1
    
    if count_one >= 2:
        count_game = count_game + 1
    count_one = 0
print(count_game)
