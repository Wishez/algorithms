from TimeTrial import TimeTrial
import sys
# Take array of N elements and search the sum of four elements equals zero.
# My algorithm is slowpoke, it seems i'm too.
def FourSum(a):
	c = 0
	N = len(a)
	h, e, l, p = 0, 0, 0, 0
	while h < N:
		e = h + 1
		while e < N:
			l = e + 1
			while l < N:
				p = l + 1
				while p < N:
					if a[h] + a[e] + a[l] + a[p] == 0:
						c += 1
					p += 1
				l += 1
			e += 1
		print(h)
		h += 1


	return c

if __name__ == '__main__':
	lim = int(sys.argv[1])
	test = TimeTrial(target=FourSum, limit=lim)
	test()

# python FourSum.py 1000