guest = str(input())
host = str(input())
letters = str(input())
total = guest + host
count = 0
if len(total) == len(letters):
  for i in total:
    if letters.count(i) < total.count(i):
      count += 1
else:
  count += 1
if count == 0:
  print("YES")
else:
  print("NO") 
