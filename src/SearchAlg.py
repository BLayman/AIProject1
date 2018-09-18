from src.Node import Node
from src.DFS import DFS

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

map = [] # data structure to store map information during search
frontier = []

# read in file to fill in map
lines = [line.rstrip('\n') for line in open('mediumMaze.txt')]

for i in range(len(lines)):
    row = []
    # iterate through characters
    for j in range(len(lines[i])):
        # create node
        node = Node(lines[i][j], i, j)
        # if start node, append to frontier
        if(lines[i][j] == 'P'):
            frontier.append(node)
        # append to row of map
        row.append(node)
    map.append(row)

#printMap(map)

# establish references to neighbors for each node
for row in map:
    for node in row:
        # add neighbors
        x = node.xCoor
        y = node.yCoor
        for i in range(y-1, y + 2):
            for j in range(x - 1,x + 2):
                # if we are not using the coordinates of the center node, and it's in bounds, and it's not a wall
                # then add it's neighbor to it
                if(not ((i == y) and (j == x)) and i >= 0 and j >= 0 and i < len(map) and j < len(row) and not map[i][j].char == '%'):
                    node.addNeighbor(map[i][j])

# printNeighbors(map)

# run depth first search
dfs = DFS(map, frontier)
dfs.search()




