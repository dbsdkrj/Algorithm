#옆집과 색깔이 달라야 함;  R, G, B 中 1택
#최소 비용이 들어야 함
N = int(input())
home = []
for _ in range(N):
    home.append(list(map(int, input().split())))
        #home[[0번 red, green, blue], [1번red, green, blue] .. ]
        #home[1][0] == 1번집의 red 비용

for j in range(1,N):  #j는 1번집부터 마지막 집까지
    # j번째 집이 빨강색일 때 이전 비용 합과 j번째 집의 총 비용
    home[j][0] = min(home[j-1][1], home[j-1][2]) + home[j][0]
    # j번째 집이 초록색일 때
    home[j][1] = min(home[j-1][0], home[j-1][2]) + home[j][1]
    # j번째 집이 파란색일 때
    home[j][2] = min(home[j-1][0], home[j-1][1]) + home[j][2]

#마지막집 차례에서 총 비용 구하기
print(min(home[N-1][0],home[N-1][1],home[N-1][2]))