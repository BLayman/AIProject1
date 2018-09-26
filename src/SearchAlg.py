from src.Node import Node
from src.Search import DFS
from src.Search import BFS

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
lines = [line.rstrip('\n') for line in open('largeMaze.txt')]

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
#dfs = DFS(map, frontier)
bfs = DFS(map, frontier)
bfs.search()




