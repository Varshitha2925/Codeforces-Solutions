n = int(input())
x = list(map(int,input().split()))[1:]
y = list(map(int,input().split()))[1:]
x.extend(y)
l = []
for i in set(x):
  if i == 0:
    x.remove(i)   
if len(set(x)) == n:
  print("I become the guy.")
else:
  print("Oh, my keyboard!")  
