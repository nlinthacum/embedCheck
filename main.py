
from itertools import permutations
import copy


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
    #make smaller Node the starting Node
    if startNode > endNode:
        tmp = startNode
        startNode = endNode
        endNode = tmp

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
    # make smaller Node the starting Node
    if startNode > endNode:
        tmp = startNode
        startNode = endNode
        endNode = tmp

    if not Nodes[startNode].points[endNode]:
        return False
    return True


def MakeCombination(permutation, numNodes):
    Mapping = {}
    for eachNode in range(numNodes):
        Mapping[eachNode] = permutation[eachNode]
    return Mapping




class Node():
    def __init__(self, numNodes):
        self.points = [True] * numNodes





if __name__ == '__main__':

 #sets up input are vars
    entered = CollectInput()
    numNodes = entered.numNodes
    edges = entered.edges
    Nodes = SetupNodes()


    perm = list(permutations(list(range(numNodes)), numNodes))
    # go through all combos
    for permutation in perm:
        combo = MakeCombination(permutation, numNodes)

        edgesManip = copy.deepcopy(edges)

        #transform the edges
        for i in range(len(edgesManip)):
            Nodes = SetupNodes()  # reset the edges
            edgesManip[i][0] = combo[edges[i][0]]
            edgesManip[i][1] = combo[edges[i][1]]

        # try all of the edges
        edge_idx = 0
        for edge in edgesManip:
            passORfail = CheckEdge(edgesManip[edge_idx][0], edgesManip[edge_idx][1], Nodes)
            if not passORfail:
                print(f"The edge {edges[edge_idx]} failed on the transformed edge ordering: {combo}")
                break
            Nodes = UpdateNodesAvailablility(edgesManip[edge_idx][0], edgesManip[edge_idx][1], numNodes, Nodes)
            edge_idx += 1

        if passORfail:  # this will be true when completed are edges for an ordering
            print(f"The ordering {combo} worked")


















