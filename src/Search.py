class Search:
    def __init__(self, map, frontier):
        self.map = map
        self.frontier = frontier

    # print maze to make sure map has been filled
    def printMap(self):
        for row in self.map:
            for node in row:
                print(node.char, end='')
            print()
    def add(self, node):
        self.frontier.append(node)
    def search(self):
        searchComplete = False
        while not searchComplete:
            # Remove a node from the frontier given the search's specifications
            frontierNode = self.remove()
            frontierNode.char = 'X'  # . indicates space has been visited
            print(frontierNode.distanceFromGoal)
            for neighbor in frontierNode.neighbors:
                # if neighbor hasn't already been visited
                if(not neighbor.visited):
                    neighbor.visited = True
                    neighbor.foundBy = frontierNode
                    # the player can only move to blank spots
                    if neighbor.char == ' ':
                        # push neighbor onto frontier stack
                        self.add(neighbor)
                    elif neighbor.char == '*':
                        searchComplete = True
            self.printMap()
            print("\n")
            frontierNode.char = '.'
        path = False
        nextNode = frontierNode
        while not path:
            nextNode.char = 'P'
            nextNode = nextNode.foundBy
            if nextNode.startNode:
                path = True
        self.printMap()

class DFS(Search):
    #The order in which nodes are removed from the stack
    def remove(self):
        return self.frontier.pop()

class BFS(Search):
    def remove(self):
        return self.frontier.pop(0)

class GreedyBest(Search):
    def remove(self):
        return self.frontier.get()[1]
    def add(self, node):
        self.frontier.put((node.distanceFromGoal, node))

class aStar(Search):
    def remove(self):
        return self.frontier.get()[1]
    def add(self, node):
        self.frontier.put(((node.distanceFromGoal + node.distanceFromStart), node))