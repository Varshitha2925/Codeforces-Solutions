def sortString(s): 
    return ''.join(sorted(s)) 
gn = input()
rn = input()
lf = input()
gr = gn+rn
gr = sortString(gr)
lf = sortString(lf)
if gr == lf:
    print("YES")
else:
    print("NO")
