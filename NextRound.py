
n , k = map(int,input().split())
L = input().split()
temp = int(L[k-1])
count = 0
for i in range(0,len(L)):
    if int(L[i]) >= temp and int(L[i]) > 0 :
        count += 1
print(count)
