import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

preorder = []
while 1:
    try:
        preorder.append(int(input()))
    except:
        break

#루트노트보다 크면 오른쪽, 작으면 왼쪽
        #재귀함수로 반복
def to_postorder(start, end):
    if start>end:
        return
    root = end + 1
    for i in range(start+1, end+1):
        if preorder[i]>preorder[start]:
            root = i
            break
    to_postorder(start+1, root-1)
    to_postorder(root, end)
    print(preorder[start])

to_postorder(0, len(preorder)-1)
