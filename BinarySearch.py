from random import randint
import sys
from TimeTrial import TimeTrial

class BinarySearch():
	def __init__(self, array):
		self.arr = sorted(array)
		self.key = 0
		self.index = -1

	def __call__(self, l=0, m=0, r=0):
		
		# Init right side of array and array's middle side.
		# If not a zero, than m equal a given argument in the function.
		# print('l: %s, m: %s, r: %s' % (l, m, r))
		if r == 0 and m == 0:
			r = len(self.arr) - 1
			m = int(r / 2)

		# print('key: %s, element: %s, match: %s' % (self.key, self.arr[m], self.key == self.arr[m]))
		if self.key == self.arr[m]: 
			self.index = m
			return
		if r == m or l == m:
			if self.key == self.arr[l + 1]:
				m = l + 1
			elif self.key == self.arr[r - 1]:
				m = r - 1
			else:
				print('Nothing found;(')
				self.index = -1
				return

			self.index = m
			return
			

		x = m
		if self.key > self.arr[m]:
			m = r - int((r - l) / 4)
			l = x
		else:
			m = l + round((r - m) / 2)
			r = x

		self(l, m, r)

	def search(self, key):
		self.key = key
		self()
		return self.index

if __name__ == '__main__':
	N = int(sys.argv[1])
	key = int(sys.argv[2])

	print('seraching:', key)
	a = [randint(0, 1000) for x in range(N)]
	bs = BinarySearch(a)
	# index = bs.search(key)
	tt = TimeTrial(target=bs.search, args=(key,))
	tt.simpleTestTime()
	index = bs.index
	print('index: %s, value: %s, length of array\'s elements: %s' % (index, bs.arr[index], N))