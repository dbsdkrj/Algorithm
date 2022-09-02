from itertools import permutations

def solution(k, dungeons):
    #주어진 던전 나열하기 (던전수!)
    result=[]

    temp=permutations(dungeons,len(dungeons))
    for j in temp:
        tk = k
        cnt=0
        for p in j:
            if tk>=p[0]:
                tk-=p[1]
                cnt+=1

        result.append(cnt)

    answer = max(result)
    return answer