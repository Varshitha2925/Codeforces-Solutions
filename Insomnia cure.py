k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())
ls = [k, l, m, n]
lsf = []
for i in range(1, d + 1):
    for ele in ls:
        if (i % ele == 0):
            lsf.append(i)
print(len(set(lsf)))
