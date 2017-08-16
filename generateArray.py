from random import randint 


def generateArray(N):	
	return [randint(1, N) for x in range(N)]
		