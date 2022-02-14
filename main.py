
from itertools import permutations


class Input:
    def __init__(self, edges, numNodes):
        self.edges = edges
        self.numNodes = numNodes



def PrintNodes():
    for i in range(numNodes):
        print(f"Node {i}: " + str(Nodes[i].points))

def CollectInput():
    numNodes = int(input("Enter number of nodes: "))
    numEdges = int(input("Enter number of edges: "))
    edges = [[0 for x in range(2)] for y in range(numEdges)]

    for x in range(numEdges):
        edges[x][0] = int(input("Enter starting node: "))
        edges[x][1] = int(input("Enter ending node: "))

    entered = Input(edges, numNodes)
    return entered


#makes list of nodes with points set to true
def SetupNodes():
    nodesFree = [Node(numNodes) for i in range(numNodes)]
    return nodesFree

def UpdateNodesAvailablility(startNode, endNode, numNodes, Nodes):

    #turn nodes in between to false
    for i in range(startNode + 1, endNode):
        for j in range(endNode + 1, numNodes):
            Nodes[i].points[j] = False

    #before can't go in between new edge
    for i in range(0, startNode):
        for j in range(startNode + 1, endNode):
            Nodes[i].points[j] = False
    return Nodes



def CheckEdge(startNode, endNode, Nodes):
    if not Nodes[startNode].points[endNode]:
        return False
    return True









class Node():
    def __init__(self, numNodes):
        self.points = [True] * numNodes





if __name__ == '__main__':

 #sets up input are vars
    entered = CollectInput()
    numNodes = entered.numNodes
    edges = entered.edges
    Nodes = SetupNodes()



#try all of the edges
    for edge in edges:
        passORfail = CheckEdge(edge[0], edge[1], Nodes)
        if not passORfail:
            print(f"The edge {edge} failed")
            break
        Nodes = UpdateNodesAvailablility(edge[0], edge[1], numNodes, Nodes)

 ##make dictionary
    perm = list(permutations(list(range(numNodes)), numNodes))


    #go through all combinations
    Mapping = {}
    for permutation in perm:
        print(f"Permutation: {permutation}")
        for eachNode in range(numNodes):
            Mapping[eachNode] = permutation[eachNode]
        print(Mapping)












