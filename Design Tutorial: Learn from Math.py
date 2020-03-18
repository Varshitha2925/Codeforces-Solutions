def findNums(n): 
	if (n % 2 == 0): 
		print("4 ", (n - 4), end = " ") 
	else: 
		print("9 ", n - 9, end = " ") 
n = int(input())
findNums(n) 
