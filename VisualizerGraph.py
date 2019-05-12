#w1673661 - UOW no
#2017063 - IIT student no
#Name - chandanam bandara (uow name)
# oshini ruksala bandara


import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot, draw, show


class Visualizer:
    #variables defined X-Y Layout as xyl, Orginal matrix of the net work flow as org_mtrx, Residual network as res,marix as mtrx
    def __init__(self, mtrx, fN, len, wid, xyl=None,org_mtrx=None, res=False):
        #make know xNetwork graph for a known structure
        #nx.Digraph, stores nodes and edges with optional data or attributes and it holds directed edges
        self.fG = nx.to_networkx_graph(mtrx, create_using=nx.DiGraph);
        #plot for the network and figure number for that
        self.plotFN(fN)
        #matrix of the network
        self.mtrx = mtrx
        #layout of the flow
        self.p = None
        #residual
        self.res = res
        #original matrix of the network flow
        self.org_mtrx = org_mtrx
        if xyl is None:
            #ggraph function,object inheriting
            #this function creating layout for the plot based on the graph
            self.createL()
        else:
            #flow the layout to xy Layout
            self.p = xyl
            #setting capacities for edges
        self.setEC(len, wid)
        #edge two-tuple of the text label, edges_label is a keyword
        #creating labels for edges
        eLables = self.createEL()
        #creating a value for nodes, need to number every node to take the augmenting path
        val = self.createNV()
        #flow graph for a flow layout,
        #dict of labels keyed on the edges will give the return
        nx.draw_networkx_edge_labels(self.fG, self.p, edge_labels=eLables)
        #dict of labels keyed on the nodes will give the return
        nx.draw_networkx_labels(self.fG, self.p)
        #line collection of edges will give the return
        nx.draw_networkx_edges(self.fG, self.p, arrows=True)
        #draw the g graph with the matplotlib
        nx.draw(self.fG, self.p, node_color=val, node_size=400, edge_cmap=plt.cm.Reds)


#creating labels for edges
    def createEL(self):
        eLables = {}
        for s_node, d_node, dictionary in self.fG.edges(data=True):
            eLables[(s_node, d_node)] = (dictionary['capacity'], dictionary['flow'])

        return eLables;
#creating values for nodes
    def createNV(self):
        val = [1.0 for node in self.fG.nodes()]
        return val
#creating network flow plot
    def plotFN(self, fN):
        plt.figure(fN)
#display the plot
    def plotShow(self):
        plt.show()
# creating layout
    # for the X and Y flow layout
    def createL(self):
        self.p = nx.spring_layout(self.fG)
#setting capacities for edges
    def setEC(self, len, wid):

#for the nodes in the range of width,
        for nd in range(wid):
            #and i, which is in the range of length
            for i in range(len):
                if self.mtrx[nd][i] > 0:
                    # in original matrix
                    #before executing through the FordFulkerson algorithm
                    #node which is searched currently and the value of i is zero
                     #it says this is a flow value
                    if (self.org_mtrx is not None and self.mtrx[nd][i] > 0 and self.org_mtrx[nd][ i] == 0):
                        self.fG[nd][i]['flow'] = self.mtrx[nd][i]
                        self.fG[nd][i]['capacity'] = self.org_mtrx[i][nd]
                    else:
                        self.fG[nd][i]['flow'] = 0
                        self.fG[nd][i]['capacity'] = self.mtrx[nd][i]

   #getting flow graph
    def get_fG(self):
        #returning flow graph
        return self.fG
#setting layout
    def setL(self, p):
        #returning flow layout
        self.p = p
#getting layout
    def getL(self):
        #returning flow layout
        return self.p