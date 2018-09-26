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
            frontierNode.char = '.'  # . indicates space has been visited
            for i in range(len(frontierNode.neighbors)):
                # if neighbor hasn't already been visited
                if(not frontierNode.neighbors[i].visited):
                    frontierNode.neighbors[i].visited = True
                    # the player can only move to blank spots
                    if(frontierNode.neighbors[i].char == ' '):
                        # push neighbor onto frontier stack
                        self.frontier.append(frontierNode.neighbors[i])
                    elif (frontierNode.neighbors[i].char == '*'):
                        searchComplete = True
            self.printMap()
            print("\n")

    def remove(self):
        pass

class DFS(Search):
    #The order in which nodes are removed from the stack
    def remove(self):
        return self.frontier.pop()

class BFS(Search):
    def remove(self):
        return self.frontier.pop(0)






