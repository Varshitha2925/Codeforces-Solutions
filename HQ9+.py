def solve(s):
    ip = "HQ9"
    for i in range(len(s)):
        if s[i] in ip:
            return "YES"
    return "NO"
s = input()
print(solve(s))
