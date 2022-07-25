n = int(input())  #최대 개수 입력 (nxn)

arr = []
for _ in range(n):  #n번동안
    colors = list(map(str, input()))  #n개의 색 입력
    arr.append(colors)  #arr에 문자열 추가

max_count = 0  #최종 최대 개수

'''
 열
[＊] [＊] [＊] 행
[＊] [＊] [＊]
[＊] [＊] [＊]
'''
def width(): #가로 방향 최대 개수 구하는 함수
    global max_count

    for i in range(n):  #행 번호
        count_width = 1  #가로방향 최대 개수
        for k in range(n-1): #열 번호
            if arr[i][k] == arr[i][k+1]: #인접한 두 칸의 색이 같으면
                count_width += 1 #가로방향 최대 개수에 +1
                max_count = max(max_count, count_width) #최종 최대 개수는 가로방향 최대개수와 기존 최대개수 중 높은 값
            else:
                count_width = 1 #인접한 칸의 색이 다르면 1

def height(): #세로 방향 최대개수 구하는 함수
    global max_count

    for i in range(n):  #열 번호
        count_height = 1  #세로방향 최대 개수
        for k in range(n-1):  #행 번호
            if arr[k][i] == arr[k+1][i]:  #세로로 인접한 칸의 색이 같으면
                count_height += 1  #세로방향 최대 개수에 +1
                max_count = max(count_height, max_count)
            else:
                count_height = 1

for j in range(n):  #0~(n-1)
    for p in range(n-1):  #0~(n-2)
        if arr[j][p] != arr[j][p+1]:  #같은 행에서 가로로 인접한 두 색이 다르면
            arr[j][p], arr[j][p+1] = arr[j][p+1], arr[j][p]  #두 칸에 있는 사탕 교환
            # 가로, 세로방향 최대개수 구하기
            width()
            height()
            arr[j][p+1], arr[j][p] = arr[j][p], arr[j][p+1] #원위치

        if arr[p][j] != arr[p+1][j]:  #같은 열에서 세로로 인접한 두 색이 다르면
            arr[p][j], arr[p+1][j] = arr[p+1][j], arr[p][j]
            width()
            height()
            arr[p+1][j], arr[p][j] = arr[p][j], arr[p+1][j]

print(max_count)