class Search:
    def __init__(self, map, frontier):
        self.map = map
        self.frontier = frontier
        self.expandedCounter = 0
        self.pathCounter = 1

    # print maze to make sure map has been filled
    def printMap(self):
        for row in self.map:
            for node in row:
                print(node.char, end='')
            print()

    def add(self, node):
        self.frontier.append(node)

    def remove(self):
        pass

    def search(self):
        searchComplete = False
        frontierNode = None

        while not searchComplete:
            # Remove a node from the frontier given the search's specifications
            frontierNode = self.remove()
            self.expandedCounter += 1
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
                        self.add(neighbor)
                    elif neighbor.char == '*':
                        searchComplete = True
            #self.printMap()
            print("\n")
            frontierNode.char =  "."#"(" + str(frontierNode.compareValue) + ")"
        path = False
        nextNode = frontierNode
        while not path:
            self.pathCounter += 1

            nextNode.char = 'P'
            nextNode = nextNode.foundBy
            if nextNode.startNode:
                path = True
                nextNode.char = 'S'

        self.printMap()
        print("Expanded counter: " + str(self.expandedCounter))
        print("Path counter: " + str(self.pathCounter))



    def searchAStar(self):
        searchComplete = False
        frontierNode = None

        while not searchComplete:
            # Remove a node from the frontier given the search's specifications
            frontierNode = self.remove()
            self.expandedCounter += 1

            frontierNode.char = 'X'  # . indicates space has been visited
            for neighbor in frontierNode.neighbors:
                # can't do graph search for a star
                #if(not neighbor.visited):
                #neighbor.visited = True

                # the player can only move to blank spots
                if neighbor.char == ' ':
                    # if discovering the node from this frontier node is more efficient
                    if neighbor.compareValue > frontierNode.greedyValue + frontierNode.costSoFar + 1:
                        # then set a new cost so far, and add to priority queue
                        neighbor.foundBy = frontierNode
                        neighbor.costSoFar = frontierNode.costSoFar + 1
                        # push neighbor onto frontier stack
                        self.add(neighbor)
                elif neighbor.char == '*':
                    searchComplete = True
            #self.printMap()
            print("\n")
            frontierNode.char =  "."#"(" + str(frontierNode.compareValue) + ")"
        path = False
        nextNode = frontierNode
        while not path:
            self.pathCounter += 1
            nextNode.char = 'P'
            nextNode = nextNode.foundBy
            if nextNode.startNode:
                path = True
                nextNode.char = 'S'
        print("printing map")
        self.printMap()
        print("Expanded counter: " + str(self.expandedCounter))
        print("Path counter: " + str(self.pathCounter))

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

    def add(self, node):
        self.frontier.put(node)

class aStar(Search):
    def remove(self):
        return self.frontier.get()

    def add(self, node):
        node.compareValue = node.costSoFar + node.greedyValue
        #node.char = node.compareValue
        print(node.compareValue)
        self.frontier.put(node)
