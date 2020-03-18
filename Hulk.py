n = int(input())
l = []
for i in range(1, n):
    if (i % 2 != 0):
        l.append("I hate that")
    else:
        l.append("I love that")
if (n % 2 == 0):
    l.append("I love it")
else:
    l.append("I hate it")
print(*l,sep = " ")
