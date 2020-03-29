for _ in range(int(input())):
  n , k = [int(x) for x in input().split()]
  count = 0
  if n % k == 0:
    print(0)
  else:
    x = int(n / k)
    a = k * (x + 1)
    count = a - n
    print(count)   
