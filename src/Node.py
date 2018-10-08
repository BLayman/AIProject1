'''
Brett Layman, Carsen Ball
AI Assignment 1, 10.8.18
'''


# Node class to represent a position in the maze
class Node:
    def __init__(self,char,yCoor,xCoor):
        # Character at the position in the map
        self.char = char
        # If the node has been visited
        self.visited = False
        # X coordinate of the position in the maze
        self.xCoor = xCoor
        # Y coordinate of the position in the maze
        self.yCoor = yCoor
        # List of the references to the nodes neighbors
        self.neighbors = []
        # List of nodes that have discovered the node
        self.foundBy = []
        # If the node is the start node
        self.startNode = False
        # Path cost
        self.costSoFar = 0

    # Adds reference to neighbor node
    def addNeighbor(self, newNeighbor):
        self.neighbors.append(newNeighbor)

# Sub class of Node class, used when running Greedy Best and AStar searches
class HeuristicNode(Node):
    def __init__(self, char, yCoor, xCoor):
        Node.__init__(self,char,yCoor,xCoor)
        # Used to compare nodes
        self.compareValue = 999999
        # If node is the goal node
        self.goalNode = False
        # Greedy Value, cost to the goal node
        self.greedyValue = None
        # Cost of the path taken to discover the node
        self.costSoFar = 0

    # Comparator which allows node to be used in the priority queue
    def __lt__(self, other):
        return self.compareValue < other.compareValue

    # sets compare value to distance from goal
    def setCompareValueGreedy(self, position):
        #self.compareValue = distance.euclidean((self.xCoor, self.yCoor), position)

        # manhattan distance
        self.compareValue = abs(self.xCoor - position[0]) + abs(self.yCoor - position[1])

    def setGreedyValueAStar(self, position):
        # manhattan distance
        self.greedyValue = abs(self.xCoor - position[0]) + abs(self.yCoor - position[1])



