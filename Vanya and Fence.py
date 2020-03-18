n , h = [int(x) for x in input().split()]
s = list(map(int,input().split()))
count = 0
for i in s:
  if i <= h:
    count += 1
  else:
    count += 2
print(count)      
