
def solve(m, n):
    tileArea = 2*1
    boardArea = m*n
    return int(boardArea / tileArea)

m, n = map(int, input().split(" "))
print(solve(m,n))
