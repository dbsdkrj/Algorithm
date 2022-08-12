import sys
sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

idx = [0] * (n+1) #중위순회inorder 순서 저장
for i in range(n):
    idx[inorder[i]]=i

def preorder(in_start, in_end, post_start, post_end):
    if (in_start>in_end) or (post_start>post_end):
        return

    root = postorder[post_end] #후위순회의 끝점이 루트
    print(root, end=" ")

    #중위순회회서 root 기준 왼쪽 오른쪽 개수
    left = idx[root] - in_start
    right = in_end - idx[root]

    preorder(in_start, in_start+left-1, post_start, post_start+left-1)
    preorder(in_end-right+1, in_end, post_end-right, post_end-1)

preorder(0, n-1, 0, n-1)