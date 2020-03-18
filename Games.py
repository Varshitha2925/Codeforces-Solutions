l = []
s = []
for _ in range(int(input())):
  n , k = input().split()
  l.append(n)
  s.append(k)
count = 0  
for i in l:
  count += s.count(i)
print(count)    
