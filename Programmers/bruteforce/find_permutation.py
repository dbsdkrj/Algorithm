from itertools import permutations

def prime(n):
    if n < 2:
        return False

    for j in range(2, n):
        if n % j == 0:
            return False
    return True

def solution(numbers):
    num = [i for i in numbers]
    p = []
    answer = 0
    for i in range(1, len(numbers) + 1):
        p.extend(permutations(numbers, i))
        new_n = [int("".join(i)) for i in p]

    for i in new_n:
        if prime(i):
            answer += 1

    return answer