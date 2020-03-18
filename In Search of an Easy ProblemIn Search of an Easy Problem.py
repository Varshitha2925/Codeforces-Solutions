n = int(input())
s = str(list(input().split()))
d = s.count("1")
if d != 0:
  print("HARD")
else:
  print("EASY")  
