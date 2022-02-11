
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
        #print(self.points)




if __name__ == '__main__':
    numNodes = CollectInput()
    Nodes = SetupNodes()
    #nodesFree[0].points[1] = False



    passORfail = CheckEdge(1,2,Nodes)

    #I am working here.....
    Nodes = UpdateNodesAvailablility(2, 5,numNodes, Nodes)

    for i in range(numNodes):
        print(f"Node {i}: " + str(Nodes[i].points))













