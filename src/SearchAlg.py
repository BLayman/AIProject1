'''
Brett Layman, Carsen Ball
AI Assignment 1, 10.8.18
'''

# Imports
from src.Node import Node
from src.Node import HeuristicNode
from src.Search import DFS
from src.Search import BFS
from src.Search import GreedyBest
from src.Search import AStar
from queue import PriorityQueue
import enum

# Enumerator for search techniques
class searchTechnique(enum.Enum):
    greedyBest = 0
    astar = 1
    dfs = 2
    bfs = 3




# Print maze
def printMap(map):
    for row in map:
        for node in row:
            print(node.char, end='')
        print()

# Print neighbors for each node ( for testing)

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

# Establish references to neighbors for each node
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


# Accepts a technique enumerator, and a map name as a string
# Runs the specified search technique on the specified map
def run(technique, map_name):
    # read in file to fill in map
    lines = [line.rstrip('\n') for line in open(map_name)]

    ## Greedy Best and A* ##
    if technique == searchTechnique.greedyBest or technique ==  searchTechnique.astar:
        frontierPQ = None
        map, startNode, goalCoor = heurstic_map(lines)
        addNeighbors(map)

        for row in map:
            for node in row:
                    if not node.goalNode:
                        if technique == searchTechnique.greedyBest:
                            node.setCompareValueGreedy((goalCoor[0], goalCoor[1]))
                        # A*
                        else:
                            node.setGreedyValueAStar((goalCoor[0], goalCoor[1]))
        # Makes priority queue from the frontier, also only necessary for heuristic searches
        frontierPQ = PriorityQueue()
        frontierPQ.put(startNode)

        if technique == searchTechnique.greedyBest:
            gb = GreedyBest(map, frontierPQ)
            gb.search()
            return gb.map, gb.expandedCounter, gb.pathCounter

        elif technique == searchTechnique.astar:
            aStar = AStar(map, frontierPQ)
            aStar.searchAStar()
            return aStar.map, aStar.expandedCounter, aStar.pathCounter

    ## DFS and BFS ##
    else:
        map, frontier = non_heurstic_map(lines)
        addNeighbors(map)

        if technique == searchTechnique.dfs:
            dfs = DFS(map, frontier)
            dfs.search()
            return dfs.map, dfs.expandedCounter, dfs.pathCounter

        elif technique == searchTechnique.bfs:
            bfs = BFS(map, frontier)
            bfs.search()
            return bfs.map, bfs.expandedCounter, bfs.pathCounter


# Given a map, name and results tuple prints the map to results.txt
def print_to_outfile(map, name, results):
    with open('results.txt', 'a') as out:
        out.write("%s : Nodes Expanded: %d Path Length: %d\n" % (name, int(results[0]), int(results[1])))
        for row in map:
            for node in row:
                out.write(node.char)
            out.write('\n')
        out.write('\n')
    out.close

if __name__ == '__main__':
    # use enum (see top) to choose search technique
    maze = "Medium Maze"
    maze_file = 'mediumMaze.txt'
    returned = run(searchTechnique.dfs, maze_file)

    print_to_outfile(returned[0], 'Depth First %s' % maze, returned[1:])

    returned = run(searchTechnique.bfs, maze_file)

    print_to_outfile(returned[0], 'Breadth First %s' % maze, returned[1:])

    returned = run(searchTechnique.greedyBest, maze_file)

    print_to_outfile(returned[0], 'Greedy Best %s' % maze, returned[1:])

    returned = run(searchTechnique.astar, maze_file)

    print_to_outfile(returned[0], 'AStar %s' % maze, returned[1:])

    maze = "Large Maze"
    maze_file = 'largeMaze.txt'
    returned = run(searchTechnique.dfs, maze_file)

    print_to_outfile(returned[0], 'Depth First %s' % maze, returned[1:])

    returned = run(searchTechnique.bfs, maze_file)

    print_to_outfile(returned[0], 'Breadth First %s' % maze, returned[1:])

    returned = run(searchTechnique.greedyBest, maze_file)

    print_to_outfile(returned[0], 'Greedy Best %s' % maze, returned[1:])

    returned = run(searchTechnique.astar, maze_file)

    print_to_outfile(returned[0], 'AStar %s' % maze, returned[1:])

    maze = "Open Maze"
    maze_file = 'openMaze.txt'
    returned = run(searchTechnique.dfs, maze_file)

    print_to_outfile(returned[0], 'Depth First %s' % maze, returned[1:])

    returned = run(searchTechnique.bfs, maze_file)

    print_to_outfile(returned[0], 'Breadth First %s' % maze, returned[1:])

    returned = run(searchTechnique.greedyBest, maze_file)

    print_to_outfile(returned[0], 'Greedy Best %s' % maze, returned[1:])

    returned = run(searchTechnique.astar, maze_file)

    print_to_outfile(returned[0], 'AStar %s' % maze, returned[1:])


