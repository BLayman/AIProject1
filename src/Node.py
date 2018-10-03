from scipy.spatial import distance

class Node:
    def __init__(self,char,yCoor,xCoor):

        self.char = char
        self.visited = False
        self.xCoor = xCoor
        self.yCoor = yCoor
        self.neighbors = []
        self.foundBy = None
        self.startNode = False
        self.costSoFar = 0

    def addNeighbor(self, newNeighbor):
        self.neighbors.append(newNeighbor)



class HeuristicNode(Node):
    def __init__(self, char, yCoor, xCoor):
        Node.__init__(self,char,yCoor,xCoor)

        self.compareValue = 999999
        self.goalNode = False
        self.greedyValue = None
        self.CostSoFar = 9999999

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



