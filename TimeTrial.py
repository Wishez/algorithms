from datetime import datetime
import time
from random import randint
from test import  TwoDifferent 
from pprint import pprint

def now():
	return time.asctime()

class TimeTrial():
	def __init__(self, target, limit=10000, args=(), startTime=datetime.now()):
		self.func = target
		self.N = []
		self.startTime = startTime
		self.endTime = 0
		self.prev = 0
		self.limit = limit
		self.args = args

	def start(self):
		self.startTime = datetime.now()
		r = self.func(self.N, *self.args)
		self.endTime = datetime.now()
		print('result: %s' % r)

	def __call__(self):
		array = 250
		self.prev = datetime.now()
		print('begin at =>', self.prev)
		last_result = 0
		while array < self.limit:
			self.N = [randint(1, array) for x in range(array)]
			self.start()
			time = self.countTime()
			current_result = self.startTime.second/self.prev.second

			print('%s - %s - %s' % (len(self.N), time, current_result))

			if not current_result == 1.0 and current_result == last_result: break

			last_result = current_result
			array *= 2
	# Use it if a function doesn't need to use some arguments.
	def simpleTestTime(self):
		self.func(*self.args)
		self.endTime = datetime.now()
		time = self.countTime()
		print('%s' % time)

	def countTime(self):
		return self.endTime - self.startTime


if __name__ == '__main__':
	trial = TimeTrial(target=TwoDifferent)
	trial()
	

