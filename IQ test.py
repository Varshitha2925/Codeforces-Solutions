n = int(input())
s = list(map(int,input().split()))[:n]
even = 0
eveni = 0
odd = 0
oddi = 0
for i in range(n):
  if s[i] % 2 == 0:
    even += 1
    eveni = i
  else:
    odd += 1
    oddi = i
if even == 1:
  print(eveni + 1)
else:
  print(oddi + 1)        
