n = int(input())

for _ in range(n):
    vps = []
    ps = input()

    for i in ps:
        if i == "(":
            vps.append(1)
        else:
            if len(vps) == 0:
                print("NO")
                break
            else:
                vps.pop()
    else:
        if len(vps)==0:
            print("YES")
        else:
            print("NO")