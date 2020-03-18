n = input().split("+")
l = []
for i in n:
  x = int(i)
  l.append(x)
s = sorted(l)
print(*s,sep = '+')  
