
def CollectInput():
    numNodes = int(input("Enter number of nodes: "))
    numEdges = int(input("Enter number of edges: "))
    edges = [[0 for x in range(2)] for y in range(numEdges)]

    for x in range(numEdges):
        edges[x][0] = int(input("Enter starting node: "))
        edges[x][1] = int(input("Enter ending node: "))
    #print(edges)
    return numNodes

def SetupNodes():
    nodesFree = [Node(numNodes) for i in range(numNodes)]
    for i in range(numNodes):
        print(nodesFree[i].points)


class Node():
    def __init__(self, numNodes):
        self.points = [True] * numNodes
        #print(self.points)


if __name__ == '__main__':
    numNodes = CollectInput()
    SetupNodes()








