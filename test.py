def TwoDifferent(arr, *args):
	c = 0
	for x in arr:
		for i in arr:
			if (x - i) == 0:
				c += 1
	return c


