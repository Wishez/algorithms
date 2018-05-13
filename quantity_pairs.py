from generateArray import generateArray
from timeTrial import timeTrial

def quantity_pairs(arr):

	arr = sorted(arr, reverse=True)
	N = len(arr)
	pairs = 0
	x = 0
	while x < N: 
		i = x + 1
		while i < N and arr[x] == arr[i]:
			pairs += 1
			i += 2
		x = i

	return pairs

if __name__ == '__main__':
	# arr = generateArray(1000000)
	testQP = timeTrial(quantity_pairs, 10000000)
	testQP()

