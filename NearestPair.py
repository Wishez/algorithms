from TimeTrial import TimeTrial
from pprint import pprint

# Search different of pair which doesn't equal other pairs. 
def NearestPair(a, *args):
	# print(a)
	N = len(a)
	# It Contains element one and element two are a pair. 
	pair = {
		'1': {
			'index': -1,
			'value': -1
		},
		'2': {
			'index': -1,
			'value': -1
		}
	}

	h, o =  0, 0

	for w in range(N):
		h = w + 1
		while h < N:
			n = h + 1
			o = h + 2

			e1 = a[w]
			e2 = a[h]
			e3 = a[n]
			e4 = a[o]

			if e1 - e2 > e3 - e4:
				break
			else:
				pair['1']['value'] = e1
				pair['1']['index'] = w
				pair['2']['value'] = e2
				pair['2']['index'] = h

			h += 1

	return pair

if __name__ == '__main__':
	test = TimeTrial(target=NearestPair)
	test()