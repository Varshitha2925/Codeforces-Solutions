
n = int(input())
s = input()[:n]
l = "abcdefghijklmnopqrstuvwxyz"
s1 = ""
s = s.lower()
s = set(s)
s = sorted(s)
s = s1.join(s)
if s == l:
    print("YES")
else:
    print("NO")
