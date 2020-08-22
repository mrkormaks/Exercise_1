def squirrel(N):
	factorial = 1
	while N > 1:
		factorial *= N
		N -= 1
	res = factorial
	while res > 9:
		res //= 10
	return res
