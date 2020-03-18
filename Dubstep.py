
s = str(input())
d = s.replace("WUB"," ")
e = d.strip(" ")
print("".join(e))
or
print(" ".join(input().split("WUB")).strip(" "))
