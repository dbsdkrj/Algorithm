# numbers = [4,1,2,1]

def solution(numbers, target):
    answer = 0
    queue = [[numbers[0],0], [-1*numbers[0],0]]  # [4, 0] , [-4, 0]
        #시작은 ±첫번째원소부터..
    n = len(numbers)  #원소 개수 = 4
    while queue:  #queue가 비어있을 때까지
        temp, idx = queue.pop() #맨 오른쪽 리스트 pop [-4, 0] -> temp=-4, idx=0
        idx += 1 #인덱스 1 증가
        if idx < n: #인덱스가 원소 개수보다 작다면 queue에 append
            queue.append([temp+numbers[idx], idx])  #지금원소 + 다음원소 = -4 + 1
            queue.append([temp-numbers[idx], idx])  #지금원소 - 다음원소 = -4 - 1
        else:  #인덱스가 원소 개수랑 같은데!! 같 은 데 !!! 즉, idx=4
            if temp == target: #temp가 target이면 즉, 현재 원소가 temp면
                answer += 1  #정답수 +1
    return answer