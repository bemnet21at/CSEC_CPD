n = int(input())
team = []
games = 0
for _ in range(n):
    team.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if team[i][0] == team[j][1]:
            games += 1

print(games)
