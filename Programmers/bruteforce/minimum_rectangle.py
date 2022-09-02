def solution(sizes):
    w=max(max(sizes[i]) for i in range(len(sizes)))
    h=max(min(sizes[i]) for i in range(len(sizes)))
    return w*h

'''
max(sizes[i]) --> 각 명함의 가로 세로 중에 큰 값
max(max(sizes[i]))  -->  전체 길이 중 가자 ㅇ큰값

min(sizes[i]) --> 각 명함의 가로 세로 중에 작은값

'''