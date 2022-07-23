# 일곱 난쟁이

# Fail😥
arr = [int(input()) for _ in range(9)]
# 경우의 수는 9명의 난쟁이 中 7명을 뽑아서 더해야되니까
# 9C7 = 9C2 = 72/2 = 36

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if (sum(arr) - arr[i] - arr[j]) == 100:
            for k in range(9):
                if k == i or k == j:
                    continue
                else:
                    print(arr[k])

# Answer
n = 9
arr = [int(input()) for _ in range(n)]
arr.sort()

for i in range(n):
    for j in range(i + 1, n):
        if sum(arr) - (arr[i] + arr[j]) == 100:
            for k in range(9):
                if i == k or j == k:
                    continue
                print(arr[k])
            exit()

print('\n'.join(map(str, arr)))

# https://ywtechit.tistory.com/133


