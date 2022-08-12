import sys
input = sys.stdin.readline
n = int(input())
tree = dict()

for _ in range(n):
    node, left, right = map(str, input().split())
    tree[node] = left, right

def preorder(x):  #CLR
    if x != ".":
        print(x, end="")
        preorder(tree[x][0])
        preorder(tree[x][1])

def inorder(x):  #LCR
    if x!= ".":
        inorder(tree[x][0])
        print(x, end="")
        inorder(tree[x][1])

def postorder(x):  #LRC
    if x!= ".":
        postorder(tree[x][0])
        postorder(tree[x][1])
        print(x, end="")

preorder("A")
print()
inorder("A")
print()
postorder("A")