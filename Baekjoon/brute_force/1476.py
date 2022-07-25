#날짜 계산
#E, S, M 증가시키면서 주어진 값과 일치할 때까지 카운트

E,S,M = map(int,input().split())
Ex, Sx, Mx = 0, 0, 0  #각각 지정
cnt = 0

while 1:   #max : 7980
    Ex += 1
    Sx += 1
    Mx += 1
    cnt += 1
    if Ex > 15:
        Ex = 1
    if Sx > 28:
        Sx = 1
    if Mx > 19:
        Mx = 1
    if Ex == E and Sx == S and Mx == M:
        break

print(cnt)