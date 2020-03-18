
s = str(input())
a = str(input())
s = s[::-1]
if s == a and len(s)<=100 and len(s)>0:
  print("YES")
elif len(s)>100:
  print("NO") 
else:
  print("NO")  
