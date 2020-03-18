n, k = list(map(int, input().split()))
tl = 240 - k
c = 0
for i in range(1,n+1):
	if tl - (5 * i) >= 0:
		tl -= 5 * i
		c += 1
print(c)
