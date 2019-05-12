
#w1673661 - UOW no
#2017063 - IIT student no
#Name - chandanam bandara (uow name)
# oshini ruksala bandara

import numpy
import random


class ADJMatrix:
	#creating variables called,len=length, wid=width and DBD=denybidirrectional
	def __init__(self, wid, len,DBD=True):
		#self represent object or same instance of the class
		self.mtrx = numpy.zeros((len, wid))
		#this represent the number of random edges per node
		NoEdgesPerNode = (len/2)
		#for node in the range of, all nodes minus one,
		for nd in range(len-1):
			#PrandomV will make sure that, it will not fill the same random value last time,
			#PrandomVal represent the previous random value
			PrandomVal = -1
			for i in range(int(NoEdgesPerNode)):
				# random.randit use for return random integers, 1 means the lowest number and len-1 mean the highest number
				r = random.randint(1, len-1)
				# diagonal of this graph is stay as zero
				#this will be a trouble for small graph which have only one node
				#r==nd is here to avoid the diagonal, r==PrandomVal to avoid same value to be overridden, mtrx[r][nd] to avoid the opposite(bidirectional)connection
				while r == nd or (nd ==1 and r == PrandomVal)  or (DBD and self.mtrx[r][nd] > 0) :
					# random.randit use for return random integers
					r = random.randint(1, len-1)

				# Random capacity value should be between 5 and 20
				r2 = random.randint(5, 20)
				self.mtrx[nd][r] = r2
				#Previous random value is equalling to r, which is taken as node=nd.
				PrandomVal = r
#getting matrix
	def get_mtrx(self):
		#returning matrix which is created using nodes,edges and capacities
		return self.mtrx
