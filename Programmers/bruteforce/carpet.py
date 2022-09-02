def solution(brown, yellow):
    all=brown+yellow
    for x in range(3,all): #x가 될 수 있는 모든 값
        if all%x==0:  # all이 x로 나누어떨어지면 가로길이 가능
            y=all//x  # y는 세로길이
        #(x,y)
            if yellow == (x-2)*(y-2): # 노란색의 가로길이는 x에서 2뺀 값, 노란색의 세로길이는 y에서 2뺀값
                    #주어진 정답의 노란색 칸의 개수는 (x-2)*(y-2)...
                return [y,x]

#다시풀어봄 (틀림. 런타임에러)
def solution(brown, yellow):
    answer = []
    # yellow의 가로를 yw, 세로를 yh라고 할 때
    # yw*yh=yellow
    # 카펫 가로 w, 세로 h라고 할때
    # w*h=brown+yellow
    # w = yellow의 가로길이 +2
    # h = yellow의 세로길이 +2
    # yellow의 칸 수 = yellow 가로길이*yellow 세로길이
    # = (w-2) * (h-2)
    all = yellow + brown
    for w in range(3, all):
        if all % w == 0:
            h = all / w

        if yellow == (w - 2) * (h - 2):#이거때문이었슈..
            answer.append(h)
            answer.append(w)
            break

    return answer

#오답수정
def solution(brown, yellow):
    answer=[]
    all = yellow+brown
    for w in range(3,all):
        if all%w==0:
            h=all//w
            if yellow == (w-2)*(h-2):
                answer.append(h)
                answer.append(w)
                break

    return answer
