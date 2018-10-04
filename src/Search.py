'''
Brett Layman, Carsen Ball
AI Assignment 1, 10.8.18
'''


# Search class used to encapsulate the frontier and map when running searches
class Search:
    def __init__(self, map, frontier):
        self.map = map
        self.frontier = frontier
        # Counts the number of nodes expanded
        self.expandedCounter = 0
        # Counts the number of nodes in the found path
        self.pathCounter = 1

    # print maze to make sure map has been filled
    def printMap(self):
        for row in self.map:
            for node in row:
                print(node.char, end='')
            print()

    # Adds a node to the frontier
    def add(self, node):
        self.frontier.append(node)

    def remove(self):
        pass

    # Method to run the search algorithm, removes nodes from the frontier, and adds neighbors to the frontier
    # Updates map when goal node has been found
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
            print("\n")
            frontierNode.char =  "."#"(" + str(frontierNode.compareValue) + ")"
        path = False
        nextNode = frontierNode
        # Changes each node in the path found to be visually represented as a P
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

# Sub class of Search to encapsulate the functionality specific to DFS
class DFS(Search):
    # Removes a node from the frontier
    def remove(self):

        return self.frontier.pop()
# Sub class of Search to encapsulate the functionality specific to BFS
class BFS(Search):
    # Removes a node from the frontier
    def remove(self):
        return self.frontier.pop(0)

# Sub class of Search to encapsulate the functionality specific to Greedy Best
class GreedyBest(Search):
    # Removes a node from the frontier
    def remove(self):
        return self.frontier.get()

    # Adds a node from the frontier
    def add(self, node):
        self.frontier.put(node)

# Sub class of Search to encapsulate the functionality specific to AStar
class AStar(Search):
    # Removes a node from the frontier
    def remove(self):
        return self.frontier.get()

    # Adds a node from the frontier
    def add(self, node):
        # Adds the cost of the path taken of the node that discovered this node to the compare value
        # Adds the manhattan distance to the goal node to the compareValue
        node.compareValue = node.costSoFar + node.greedyValue
        print(node.compareValue)
        self.frontier.put(node)
