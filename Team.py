n = int(input())
cnt1 = 0
for i in range (n):
    frnds1 = list(map(int,input().split()))[:3]
    frnds2 = str(frnds1)
    cnt2 = frnds2.count("1")
    if (cnt2 >= 2):
        cnt1 += 1
print(cnt1)

