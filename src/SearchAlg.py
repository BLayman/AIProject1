from src.Node import Node
from src.Node import HeuristicNode
from src.Search import DFS
from src.Search import BFS
from src.Search import GreedyBest
from queue import PriorityQueue
from src.Search import aStar
import enum

class searchTechnique(enum.Enum):
    greedyBest = 0
    astar = 1
    dfs = 2
    bfs = 3



## functions for testing if map is correct##

# print maze to make sure map has been filled (for testing)
def printMap(map):
    for row in map:
        for node in row:
            print(node.char, end='')
        print()

# print neighbors for each node ( for testing)
def printNeighbors(map):
    for row in map:
        for node in row:
            for neighbor in node.neighbors:
                if neighbor.wall:
                    print('%', end='')
                elif neighbor.start:
                    print('P', end='')
                elif neighbor.end:
                    print('*', end='')
                else:
                    print(' ', end='')
            print()



## code that's run ##

# Returns a map and frontier with normal nodes
def non_heurstic_map(lines):
    map = []
    frontier = []
    for i in range(len(lines)):
        row = []
        # iterate through characters
        for j in range(len(lines[i])):
            # create node
            node = Node(lines[i][j], i, j)
            # if start node, append to frontier
            if(lines[i][j] == 'P'):
                node.startNode = True
                frontier.append(node)
            # append to row of map
            row.append(node)
        map.append(row)
    return map, frontier


# Returns a map and a frontier with Heuristic Nodes
def heurstic_map(lines):
    map = []
    startNode = None
    goalCoor = None
    for i in range(len(lines)):
        row = []
        # iterate through characters
        for j in range(len(lines[i])):
            # create node
            node = HeuristicNode(lines[i][j], i, j)
            # if start node, append to frontier
            if(lines[i][j] == 'P'):
                node.startNode = True
                startNode = node
            # This won't be needed for greedy best but it seemed stupid to make a whole new function
            if (lines [i][j] == '*'):
                goalCoor = (j, i)
                node.goalNode = True
            # append to row of map
            row.append(node)
        map.append(row)
    return map, startNode, goalCoor
#printMap(map)


# establish references to neighbors for each node
def addNeighbors(map):
    for row in map:
        for node in row:
            # add neighbors
            x = node.xCoor
            y = node.yCoor

            # if we are not using the coordinates of the center node, and it's in bounds, and it's not a wall
            # then add it's neighbor to it
            i = y
            j = x - 1
            if(i >= 0 and j >= 0 and i < len(map) and j < len(row) and not map[i][j].char == '%'):
                node.addNeighbor(map[i][j])
            i = y
            j = x + 1
            if (i >= 0 and j >= 0 and i < len(map) and j < len(row) and not map[i][j].char == '%'):
                node.addNeighbor(map[i][j])
            i = y - 1
            j = x
            if (i >= 0 and j >= 0 and i < len(map) and j < len(row) and not map[i][j].char == '%'):
                node.addNeighbor(map[i][j])
            i = y + 1
            j = x
            if (i >= 0 and j >= 0 and i < len(map) and j < len(row) and not map[i][j].char == '%'):
                node.addNeighbor(map[i][j])

# printNeighbors(map)

# run depth first search

if __name__ == '__main__':

    # use enum (see top) to choose search technique
    technique = searchTechnique.bfs

    # read in file to fill in map

    lines = [line.rstrip('\n') for line in open('openMaze.txt')]

    ## Greedy Best and A* ##
    if technique == searchTechnique.greedyBest or technique ==  searchTechnique.astar:
        frontierPQ = None
        map, startNode, goalCoor = heurstic_map(lines)
        addNeighbors(map)

        for row in map:
            for node in row:
                    if not node.goalNode:
                            node.setCompareValueGreedy((goalCoor[0], goalCoor[1]))

        # Makes priority queue from the frontier, also only necessary for heuristic searches
        frontierPQ = PriorityQueue()
        frontierPQ.put(startNode)

        if technique == searchTechnique.greedyBest:
            gb = GreedyBest(map, frontierPQ)
            gb.search()

        elif technique == searchTechnique.astar:
            aStar = aStar(map, frontierPQ)
            aStar.search()

    ## DFS and BFS ##
    else:
        map, frontier = non_heurstic_map(lines)
        addNeighbors(map)

        if technique == searchTechnique.dfs:
            dfs = DFS(map, frontier)
            dfs.search()

        elif technique == searchTechnique.bfs:
            bfs = BFS(map, frontier)
            bfs.search()




