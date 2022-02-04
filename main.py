
class Node:
    def __init__(self, numberNodes):
        self.points = [True] * numberNodes
        print(self.points)


#Node1 = Node(5)


numEdges = int(input("Enter number of edges: "))
edges = [[0 for x in range(2)] for y in range(numEdges)]

for x in range(numEdges):
    edges[x][0] = int(input("Enter starting node: "))
    edges[x][1] = int(input("Enter ending node: "))

print(edges)

