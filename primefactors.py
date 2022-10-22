n=int(input())
c = 2
while(n > 1):

	if(n % c == 0):
		print(c, end="\n")
		n = n / c
	else:
		c = c + 1
