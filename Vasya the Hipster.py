a, b = list(map(int, input().split()))
sol = []
v1 = 0
v2 = 0
if b < a:
    sol.append(b)
    v1 = a - b
    v2 = int(v1 / 2)
    sol.append(v2)
elif a < b:
    sol.append(a)
    v1 = b - a
    v2 = int(v1 / 2)
    sol.append(v2)
else:
    sol.append(a)
    sol.append(0)
print(*sol,sep = " ")    
