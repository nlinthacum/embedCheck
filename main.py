
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


def ListModes():
    print("Mode 1: print the orderings that work")
    print("Mode 2: determine the book thickness")


class Node():
    def __init__(self, numNodes):
        self.points = [True] * numNodes


#lists the orderings that work and fail
def listOrderings(Nodes, edgesManip, edges, numNodes):
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

def BookThickness(Nodes, edgesManip, edges, numNodes):
    edgePerms = list(permutations(edgesManip, len(edgesManip))) #permutations of edgesManip


    for edgePerm in edgePerms:
        bookThickness = 1
        local_book_thickness = 9999999
        edge_idx = 0
        edgesInPage = []
        for edge in edgePerm:
            passORfail = CheckEdge(edgePerm[edge_idx][0], edgePerm[edge_idx][1], Nodes)
            if passORfail:
                Nodes = UpdateNodesAvailablility(edgePerm[edge_idx][0], edgePerm[edge_idx][1], numNodes, Nodes)
                edgesInPage.append(edgePerm[edge_idx])
            else:
                print(f"Book page {bookThickness} with: {edgesInPage} with the combination {combo}")
                bookThickness += 1
                Nodes = SetupNodes()  # reset the edges
                Nodes = UpdateNodesAvailablility(edgePerm[edge_idx][0], edgePerm[edge_idx][1], numNodes, Nodes) #add current node to next page
                edgesInPage = [edges[edge_idx]]

            edge_idx += 1
        print(f"Book page {bookThickness} with: {edgesInPage} with the combination {combo}")
        print(f"The book thickness for ordering {combo} is {bookThickness}")
        print("\n")

        if local_book_thickness < bookThickness:
            bookThickness = local_book_thickness



        Nodes = SetupNodes()  # reset the edges




    return bookThickness

if __name__ == '__main__':

 #sets up input are vars
    ListModes(
    )
    mode = int(input("Enter Mode: "))
    entered = CollectInput()
    numNodes = entered.numNodes
    edges = entered.edges
    Nodes = SetupNodes()
    perm = list(permutations(list(range(numNodes)), numNodes))
    min_book_thickness = 999999999
    min_thickness_ordering = []


    # go through all combos
    for permutation in perm:
        combo = MakeCombination(permutation, numNodes)

        edgesManip = copy.deepcopy(edges)

        #transform the edges
        for i in range(len(edgesManip)):
            Nodes = SetupNodes()  # reset the edges
            edgesManip[i][0] = combo[edges[i][0]]
            edgesManip[i][1] = combo[edges[i][1]]


        #case 1: list the combos that work and the ones that fail
        if mode == 1:
            listOrderings(Nodes, edgesManip, edges, numNodes)
        #case 2: determine the book thickness
        elif mode == 2:
            curThickness = BookThickness(Nodes, edgesManip, edges, numNodes)
            if curThickness == min_book_thickness:
                min_thickness_ordering.append(permutation)
            elif curThickness < min_book_thickness:
                min_thickness_ordering.clear()
                min_thickness_ordering.append(permutation)
                min_book_thickness = curThickness



    if mode == 2:
        print(f"Book Thickness: {min_book_thickness} with ordering {min_thickness_ordering}")





