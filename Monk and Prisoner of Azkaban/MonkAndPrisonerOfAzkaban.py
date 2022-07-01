n = int(input())
arr = list(map(int, input().split()))
x = [0]*n
y = [0]*n
stack = []
for i in range(n-1, -1, -1):
    while stack != [] and stack[-1][0] <= arr[i]:
        stack.pop()
    if stack != []:
        y[i] = (stack[-1][1]+1)
    else:
        y[i] = (-1)
    stack.append((arr[i],i))
stack = []

for i in range(n):
    while stack != [] and stack[-1][0] <= arr[i]:
        stack.pop()
    if stack != []:
        x[i] = (stack[-1][1]+1)
    else:
        x[i] = (-1)
    stack.append((arr[i],i))
    print(x[i]+y[i], end=" ")