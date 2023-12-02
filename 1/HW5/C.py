num_of_points = int(input())
points = []
for _ in range(num_of_points):
    points.append(list(map(int, input().split())))
num_of_trails = int(input())
trails = []
for _ in range(num_of_trails):
    trails.append(list(map(int, input().split())))

heights = [0] * num_of_points
for i in range(num_of_points - 1):
    diff = points[i][1] - points[i+1][1]
    heights[i+1] = heights[i] + diff

for trail in trails:
    elevation = 0
    if trail[0] - trail[1] < 0:
        left = trail[0] - 1
        right = trail[0]
        while left != trail[1] - 1:
            if abs(heights[left]) - abs(heights[right]) < 0:
                elevation -= abs(heights[left]) - abs(heights[right])
            right += 1
            left += 1
    elif trail[0] - trail[1] > 0:
        right = trail[0] - 1
        left = right - 1
        while right != trail[1] - 1:
            if abs(heights[right]) - abs(heights[left]) < 0:
                elevation += abs(heights[left]) - abs(heights[right])
            right -= 1
            left -= 1
    else:
        left = 0
        right = 1
        while left != len(heights) - 1:
            if abs(heights[left]) - abs(heights[right]) < 0:
                elevation -= abs(heights[left]) - abs(heights[right])
            right += 1
            left += 1
    print(elevation)
