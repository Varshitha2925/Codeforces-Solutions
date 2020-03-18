
def solve(str):
       
    return  "".join("."+char.lower() for char in str if char.lower() not in "aeiouy")

        
str = input()
print(solve(str))
