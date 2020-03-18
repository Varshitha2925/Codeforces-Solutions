def phy(vs):
    xc = yc = zc = 0
    for v in vs:
        xc += v[0]
        yc += v[1]
        zc += v[2]
    if(xc==yc==zc==0):
        return "YES"
    else:
        return "NO"
vs = []
for x in range(int(input())):
    v = list(map(int, input().split()))
    vs.append(v)
print(phy(vs))
