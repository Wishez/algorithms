from datetime import datetime


class QuickUnion():
	def __init__(self, N):
		self.N = N
		self.id = [i for i in range(self.N)]
		self.sz = [1 for i in range(self.N)]
		
	def root(self, i):
		while i != self.id[i]: 
			# Tree compression which get element x, where it is i and 
			# put it in one step before.
			self.id[i] = self.id[self.id[i]]
			i = self.id[i]

		return i

	def connected(self, p, q):
		return self.root(p) == self.root(q)

	def union(self, p, q):
		i = self.root(p)
		j = self.root(q)

		if i == j: return

		if self.sz[i] and self.sz[i] and self.sz[i] < self.sz[j]:
			self.id[i] = j
			self.sz[j] += self.sz[i];
			print('Size: %s Tree: %s' % (self.sz[j], j))
		else:
			self.id[j] = i
			self.sz[i] += self.sz[j] 
			print('Size: %s Tree: %s' % (self.sz[i], i))

		print('Connected: %s <=> %s' % (i, j))

	def start(self):
		while True:
			p = input('Exit is "" or p => ')
			if p == '':
				break
			else:
				p = int(p)

			q = int(input('q => '))

			if p >= self.N or q >= self.N:
				print('N cannot will be more than "id" length')
				self.start()
				return
			if not self.connected(p, q):
				self.union(p, q)
			else:
				print('It has already connected')

if __name__ == '__main__': 
	N = int(input('N is => '))

	assert isinstance(N, int), 'N is not a number'

	qu = QuickUnion(N)
	qu.start()

