def sort_points(points):
    return sorted(points, key=lambda x: (x[0], x[1]))

n = int(input().strip())
points = []
for i in range(n):
    x, y = map(int, input().strip().split())
    points.append((x, y))

sorted_points = sort_points(points)
for point in sorted_points:
    print(point[0], point[1])