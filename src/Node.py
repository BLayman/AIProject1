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

    def addNeighbor(self, newNeighbor):
        self.neighbors.append(newNeighbor)

class HeuristicNode(Node):
    def __init__(self, char, yCoor, xCoor):
        self.char = char
        self.visited = False
        self.xCoor = xCoor
        self.yCoor = yCoor
        self.neighbors = []
        self.foundBy = None
        self.startNode = False
        self.distanceFromGoal = None
        self.distanceFromStart = None
        self.goalNode = False

    def __lt__(self, other):
        return self.distanceFromGoal < other.distanceFromGoal

    def setDistanceTo(self, option, position):

        if option == 'start':
            self.distanceFromStart = distance.euclidean((self.xCoor, self.yCoor), position)
        elif option == 'goal':
            self.distanceFromGoal = distance.euclidean((self.xCoor, self.yCoor), position)