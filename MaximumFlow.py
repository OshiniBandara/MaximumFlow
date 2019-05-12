
#w1673661 - UOW no
#2017063 - IIT student no
#Name - chandanam bandara (uow name)
# oshini ruksala bandara


from collections import defaultdict
import numpy
import networkx as nx
import matplotlib.pyplot as plot
from matplotlib.pyplot import plot, draw, show
import random
import pylab
# using the adjacency matrix ADJMatrix class represent the graph which is with directed nodes
import ADJMatrix as adjmtrx
#using this VisualizerGraph class it returns the residual and orginal random graphs
import VisualizerGraph
import sys
import time
class MaximumFlow:
#graph and the residual graph
	def __init__(self, g,rg):
		#2D matrix graph which is representing the residual graph
		self.g = g
		self.rg= rg
		#length
		self. Len = len(g)
		#source to destination node, current  path is storing nodes
		#if there is a path, this function returns true
		#2d graph, if value is greater than zero,
		#first breadthfirstsearch, 2nd path flow of the the value,which is giv previously
		#may be reached 0 , it making the path which i spreviously executed and it stop being involving it on the current execution

#breadthfirsth search for source,sink and current path
	def BFSearch(self, sourz, desti, currentP):
		# Initalize Visited array to False
		visited = [False]*(self.Len)
		#queue of the accessed nodes
		accessedNQueue = []
		# Add source since , search start from the source
		accessedNQueue.append(sourz)
		#if the source is visited mark it as true to recognize that node is visited
		visited[sourz] = True
#while the accessed nodes of queue
		while accessedNQueue:
			# taking the first element of the queue
			# from current vertices
			currentV = accessedNQueue.pop(0)
			#Get adjacent node to the current vertice
			#enumerate will give both index and the value
			for y, value in enumerate(self.g[currentV]):
				#if the y node is visited mark it as false and value to be greater than zero
				if visited[y] == False and value > 0:
					#in the queue of the accessed nodes, node y
					accessedNQueue.append(y)
					#mark the node y as visited,by equalling it to true
					visited[y] = True
					#cuurent path is asigning to y and it equalsto current vertices
					currentP[y] = currentV
		# return the true if the path reached destination node,else return false...because the path is not completed to source to destination
		return True if visited[desti] else False

	# from source to destination this returns the maximum flow of the graph
	def FordFulkersonAlgorithm(self, sourz, sink):

		#To store the augmenting path of breadth first search
		#is storing in this array
		currentP = [-1]*(self.Len)
		#maximum flow is intializing to zero
		maxF = 0
		#and the i node to one
		i =1
		#when there is a path source to destination
		#augmenting the flow
		while self.BFSearch(sourz, sink, currentP):


			#finding the minimum value of the residual capacity,
			# which is the path, filled by the BFS
			#Or else, the path which is found, is executing to find the maximum flow of that path
			print('Augmenting Path of the NetworkFlow = '+str(i))
			#current path of the nodes
			print(currentP)
			pathF = float("Inf")
			#atake q as the sink of the collection of random nodes
			q = sink
			#while the q node is not finding the source node, loop is executing
			while(q != sourz):
				#taking the minimum value of the path, as the maximum flow of selected path
				pathF = min(pathF, self.g[currentP[q]][q])
				q = currentP[q]

			# Add path flow to overall flow
			maxF += pathF
			#displaying the augmenting paths
			print("Path Flow of the Augmenting Path =  "+str(i) + " - " +str(pathF))
			# along the augmenting path updating the capacities of edges
			#reverse edges residual capacities
			#taking w as the sink
			w = sink
			#while w is not reaching the source
			while(w != sourz):
				z = currentP[w]
				#updating the path flow
				self.g[z][w] -= pathF
				#reverse edges updating
				self.g[w][z] += pathF
				#mark it as updated graph
				self.rg[z][w] =self.g[w][z]

				w = currentP[w]
			i=i+1
			#returning the maximum flow
		return maxF


if __name__ == "__main__":

	length = int(sys.argv[1])
	width = int(sys.argv[1])
	#while the nodes are between 2 and 10 without source and sink
	while length < 2 and length > 10:
		print("Invalid Graph node length, Please Re-enter :")
		length = int(input())
		#creating object in ADJMatrix class as MA and getting length and width of nodes
	MA = adjmtrx.ADJMatrix(length,width)
	#creating the matrix of random graph
	adjmtrx =MA.get_mtrx()
	org_mtrx =numpy.copy(adjmtrx)
	#creating object in MaximumFlow class asgMF, to return to length and width of nodes
	gMF = MaximumFlow(adjmtrx, numpy.zeros((length, width)))
	#displaying the adjancecncy matrix for the random graph
	print(adjmtrx)


	#getting source as zero
	sourz = 0
	#sink as random generated nodes minus one, because it is start counting from zero
	sink = width-1

	#creator of the flow graph
	#creating object in VisualizerGraph class and returning the orginal graph in 200 number
	CreatorFG =VisualizerGraph.Visualizer(adjmtrx, 200, length, width)
	#creating flow graph, getting the flow graph to display
	FG=CreatorFG.get_fG()
	#displaying the edges of the random generated
	print("Edges of the graph = "+str(len(FG.edges())))
	#displaying the maximum flow which is calculated using FF algorithm
	#start time of execution
	startTime = time.time()
	print("Maximum  flow of the graph is = %d " % gMF.FordFulkersonAlgorithm(sourz, sink))
	#end time of execution
	endTime = time.time()
	#calculating the execution time
	excutionTime = endTime - startTime
	#displaying the time for spent to find the optimal solution
	print("excution time for the Algorithm = ")
	print(excutionTime)

	#creating object in VisualizerGraph class and returning the residual graph in number 300, using orginal matrix
	CreatorRG=VisualizerGraph.Visualizer(gMF.g, 300, length, width, CreatorFG.getL(), org_mtrx=org_mtrx)
	#creating residual flow graph and getting it to display
	RG=CreatorRG.get_fG()
	#display the plot
	CreatorRG.plotShow()


