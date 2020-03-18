n , k = [int(x) for x in input().split()]
if n % 2 == 0:
  c = n / 2
else:
  c = (n+1) / 2
if k <= c:
  print((2*k) - 1)   
else:
  if n % 2 == 0:
    print(k*2 - n)
  else:
    print(k*2 - n - 1)  
