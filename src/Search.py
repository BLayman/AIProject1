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

    def add(self, node, ignore):
        self.frontier.append(node)

    def remove(self):
        pass

    def search(self):
        searchComplete = False
        frontierNode = None

        while not searchComplete:
            # Remove a node from the frontier given the search's specifications
            frontierNode = self.remove()
            frontierNode.char = 'X'  # . indicates space has been visited
            for neighbor in frontierNode.neighbors:
                # if neighbor hasn't already been visited
                if(not neighbor.visited):
                    neighbor.costSoFar = frontierNode.costSoFar + 1
                    neighbor.visited = True
                    neighbor.foundBy = frontierNode
                    # the player can only move to blank spots
                    if neighbor.char == ' ':
                        # push neighbor onto frontier stack
                        self.add(neighbor, frontierNode.costSoFar)
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
        return self.frontier.get()

    def add(self, node, ignore):
        self.frontier.put(node)

class aStar(Search):
    def remove(self):
        return self.frontier.get()

    def add(self, node, costSoFar):
        node.compareValue += costSoFar
        print(node.compareValue)
        self.frontier.put(node)
