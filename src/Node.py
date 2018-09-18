class Node:
    def __init__(self,char,yCoor,xCoor):

        self.char = char
        self.visited = False
        self.xCoor = xCoor
        self.yCoor = yCoor
        self.neighbors = []

    def addNeighbor(self, newNeighbor):
        self.neighbors.append(newNeighbor)
