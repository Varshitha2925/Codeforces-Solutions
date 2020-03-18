def solve(n,stones):
    changes = 0
    for i in range(1,n):
        if(stones[i]==stones[i-1]):
            changes+=1    
                    
    return changes
n = int(input())
stones = input()
print(solve(n,stones))
