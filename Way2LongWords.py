n = int(input())
s = []
l = []
for _ in range(n):
  x = input()
  s.append(x)
for i in s:
  if len(i) > 10:
    d = len(i) - 2
    i = i[0] + str(d) + i[-1]
    l.append(i)
  else:
    l.append(i)  
for i in l:
  print(i)    
