
n = int(input())
l = []
for _ in range(n):
  t = int(input())
  l.append(t)
count = 1  
for i in range(n-1):
  if l[i] != l[i + 1]:
    count += 1
print(count)    
