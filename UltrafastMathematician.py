n = list(str(input()))
m = list(str(input()))

l = []
for i in range(len(n)):
  if n[i] == m[i]:
    l.append(0)
  else:
    l.append(1)
print(*l,sep = "")      
