n = int(input())
coords = [list(map(int, input().split())) for x in range(n)]
answer = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        dist1 = (((coords[i][0] - coords[j][0]) ** 2) + ((coords[i][1] - coords[j][1]) ** 2)) ** 0.5
        for k in range(j+1, n):
            dist2 = (((coords[i][0] - coords[k][0]) ** 2) + ((coords[i][1] - coords[k][1]) ** 2)) ** 0.5
            dist3 = (((coords[k][0] - coords[j][0]) ** 2) + ((coords[k][1] - coords[j][1]) ** 2)) ** 0.5
            if (dist1 == dist2 or dist1 == dist3 or dist2 == dist3) and dist3 < dist2 + dist1:
                answer += 1
print(answer)
