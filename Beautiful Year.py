def by(y):
    while(True):
        y = str(int(y) + 1)
        if(len(set(y)) == 4):
            return y
print(by(input()))
