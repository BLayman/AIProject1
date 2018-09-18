class DFS:
    def __init__(self, map, frontier):
        self.map = map
        self.frontier = frontier

    # run search algorithm
    def search(self):
        searchComplete = False
        while not searchComplete:
            # pop node off of frontier stack
            frontierNode = self.frontier.pop()
            for neighbor in frontierNode.neighbors:
                # if neighbor hasn't already been visited
                if(not neighbor.visited):
                    neighbor.visited = True
                    # the player can only move to blank spots
                    if(neighbor.char == ' '):
                        neighbor.char = '.' # . indicates space has been visited
                        # push neighbor onto frontier stack
                        self.frontier.append(neighbor)
                    elif (neighbor.char == '*'):
                        searchComplete = True
            self.printMap()
            print("\n")

    # print maze to make sure map has been filled
    def printMap(self):
        for row in self.map:
            for node in row:
                print(node.char, end='')
            print()




