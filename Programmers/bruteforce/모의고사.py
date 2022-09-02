def solution(answers):
    answer = []
    ans = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    for i in range(3):
        cnt = 0
        for j in range(len(answers)):
            if ans[i][j % len(ans[i])] == answers[j]:
                cnt += 1
        answer.append(cnt)
    a = max(answer)
    arr = []
    for i in range(3):
        if answer[i] == a:
            arr.append(i + 1)

    return arr

#다시 풀어봄
def solution(answers):
    supoza=[[1,2,3,4,5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    answer = []
    for i in range(3):
        cnt=0
        for j in range(len(answers)): #주어진 문제 개수
            if supoza[i][j%len(supoza[i])]==answers[j]:
                cnt+=1
        answer.append(cnt)
    final_answer=[]
    m = max(answer)
    for i in range(len(answer)):
        if answer[i]==m:
            final_answer.append(i+1)
    return final_answer