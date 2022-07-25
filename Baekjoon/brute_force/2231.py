'''
1부터 1000000까지 x라고 하면서
x의 각 자리수 쪼개기 -> x랑 x의 각 자리수 더해서 n이면 x 출력
'''

n = int(input())
result = 0

for i in range(1, 1000001):
    arr = list(map(int,str(i)))
    if i + sum(arr) == n:
        result = i
        break

print(result)