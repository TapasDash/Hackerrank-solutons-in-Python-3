q = []
n = int(input())
temp = 0
for _ in range(n):
    f,d = map(int,input().split(' '))
    temp = temp + (f-d)
    q.append(temp)
pos = q.index(min(q))
if pos == n-1:
    print(0)
else:
    print(pos + 1)
