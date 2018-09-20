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
    def search(self):
        searchComplete = False
        while not searchComplete:
            # pop node off of frontier stack
            frontierNode = self.remove()
            frontierNode.char = 'X'  # . indicates space has been visited
            for neighbor in frontierNode.neighbors:
                # if neighbor hasn't already been visited
                if(not neighbor.visited):
                    neighbor.visited = True
                    neighbor.foundBy = frontierNode
                    # the player can only move to blank spots
                    if(neighbor.char == ' '):
                        # push neighbor onto frontier stack
                        self.frontier.append(neighbor)
                    elif (neighbor.char == '*'):
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


    def remove(self):
        pass

class DFS(Search):
    #The order in which nodes are removed from the stack
    def remove(self):
        return self.frontier.pop()

class BFS(Search):
    def remove(self):
        return self.frontier.pop(0)






