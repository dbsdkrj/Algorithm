# # 일곱 난쟁이
#
# # Fail😥
# arr = [int(input()) for _ in range(9)]
# # 경우의 수는 9명의 난쟁이 中 7명을 뽑아서 더해야되니까
# # 9C7 = 9C2 = 72/2 = 36
#
# for i in range(len(arr)):
#     for j in range(i + 1, len(arr)):
#         if (sum(arr) - arr[i] - arr[j]) == 100:
#             for k in range(9):
#                 if k == i or k == j:
#                     continue
#                 else:
#                     print(arr[k])

# Answer
n = 9 #난쟁이 9명
arr = [int(input()) for _ in range(n)] #9명의 키를 한줄마다 입력
arr.sort() #오름차순 정렬(small->big)

for i in range(n):  # 0~8
    for j in range(i + 1, n):  # 1~9
        if sum(arr) - (arr[i] + arr[j]) == 100:  #전체합 - (두명 합)이 100이면
            for k in range(9):  # 0~8
                if i == k or j == k: #i번째와 j번째는 pass
                    continue
                print(arr[k]) #나머지 원소는 print
            exit()

# print('\n'.join(map(str, arr)))
