
def CollectInput():
    numNodes = int(input("Enter number of nodes: "))
    numEdges = int(input("Enter number of edges: "))
    edges = [[0 for x in range(2)] for y in range(numEdges)]

    for x in range(numEdges):
        edges[x][0] = int(input("Enter starting node: "))
        edges[x][1] = int(input("Enter ending node: "))
    #print(edges)
    return numNodes


#makes list of nodes with points set to true
def SetupNodes():
    nodesFree = [Node(numNodes) for i in range(numNodes)]
    return nodesFree

#def UpdateNodesAvailablility():



def CheckEdge(startNode, endNode, Nodes):
    if not Nodes[startNode].points[endNode]:
        return False
    return True








class Node():
    def __init__(self, numNodes):
        self.points = [True] * numNodes
        #print(self.points)




if __name__ == '__main__':
    numNodes = CollectInput()
    Nodes = SetupNodes()
    #nodesFree[0].points[1] = False

    Nodes[1].points[3] = False
    Nodes[1].points[4] = False

    for i in range(numNodes):
        print(Nodes[i].points)

    passORfail = CheckEdge(1,3,Nodes)

    print(f"Does edge pass: {passORfail}")











