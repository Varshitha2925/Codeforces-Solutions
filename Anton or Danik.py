n = int(input())
s = str(input())
a = s.count('A')
d = s.count('D')
if a < d:
  print("Danik")
elif a > d:
  print("Anton")
else:
  print("Friendship")  
