n = int(input())

arr = []
for _ in range(n):
    colors = list(map(str, input()))
    arr.append(colors)

max_count = 0

def width():
    global max_count

    for i in range(n):
        count_width = 1
        for k in range(n-1):
            if arr[i][k] == arr[i][k+1]:
                count_width += 1
                max_count = max(max_count, count_width)
            else:
                count_width = 1

def height():
    global max_count

    for i in range(n):
        count_height = 1
        for k in range(n-1):
            if arr[k][i] == arr[k+1][i]:
                count_height += 1
                max_count = max(count_height, max_count)
            else:
                count_height = 1

for j in range(n):
    for p in range(n-1):
        if arr[j][p] != arr[j][p+1]:
            arr[j][p], arr[j][p+1] = arr[j][p+1], arr[j][p]
            width()
            height()
            arr[j][p+1], arr[j][p] = arr[j][p], arr[j][p+1]

        if arr[p][j] != arr[p+1][j]:
            arr[p][j], arr[p+1][j] = arr[p+1][j], arr[p][j]
            width()
            height()
            arr[p+1][j], arr[p][j] = arr[p][j], arr[p+1][j]

print(max_count)