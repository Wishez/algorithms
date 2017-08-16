from random import randint
from datetime import datetime

class UF: 
	def __init__(self, N):
		self.N = N
		self.id = [i for i in range(N)]
		self.startTime = datetime.now()
		self.endTime = 0
		self.executeTime = 0

	def connected(self, p, q):
		return p == q

	def union(self, p, q):
		self.id[q] = self.id[p]


	def startDynamicConnection(self):
		while True:
			p = input('exit or p => ')

			if p == '':
				break
			else:
				p = int(p)

			q = int(input('q => '))

			pid = self.id[p]
			qid = self.id[q]
			if not self.connected(pid, qid):
				self.union(p, q)
				print('%s <-> %s' % (p, q))
			print(self.id)
			# if (index + 1) == len(self.id):
				# self.endTime = datetime.now()
				# self.executeTime = self.endTime - self.startTime

if __name__ == '__main__':
	N = int(input('N => '))

	assert isinstance(N, int), 'Not integer number'
	uf = UF(N)
	uf.startDynamicConnection()
	

		

