def search(arr, key):
    si = 0
    li = len(arr) - 1
    while si < li:
        mid = (si + li) // 2
        if key >= arr[mid]:
            si = mid + 1
        else:
            li = mid
    return si

n = int(input())
stack = []

for i in range(n):
    arr = list(map(int, input().split()))
    stack.append(arr[1:])

q = int(input())
first_min = [stack[0][0]]

for i in range(1, len(stack[0])):
    first_min.append(min(first_min[-1], stack[0][i]))

for _ in range(q):
    inp = list(map(int, input().split()))

    if inp[0] == 0:
        stack[inp[1]-1].pop()
        if inp[1] == 1:
            first_min.pop()

    elif inp[0] == 1:
        stack[inp[1]-1].append(inp[2])
        if inp[1] == 1:
            first_min.append(min(first_min[-1], inp[2]))

    else:
        chk = 0
        if stack[0] == []:
            print("NO")
            continue
        key = first_min[-1]
        for i in range(1,n):
            if stack[i] == [] or key > stack[i][-1]:
                chk = 1
                break
            key = stack[i][search(stack[i], key)]
        if chk == 0:
            print("YES")
        else:
            print("NO")