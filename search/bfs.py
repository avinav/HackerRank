#!/usr/bin/python
class Queue:
    def __init__(self):
        self.list = []
    def push(self,item):
        self.list.append(item)
    def pop(self):
        return self.list.pop(0)
    def isEmpty(self):
        return len(self.list) == 0

def    getSuccessors(state):
    (x,y) = state
    successors    =    [];
    if    (x    >=0    and    x    <    c    and    y    >=    0    and    y    <    r):
        if    (grid[y-1][x]    !=    '%'    and    y    >=    1):
            successors.append((x,y-1));
        if    (grid[y][x-1]    !=    '%'    and    x    >=    1):
            successors.append((x-1,y));
        if    (grid[y][x+1]    !=    '%'    and    x    <    c-1):
            successors.append((x+1,y));
        if    (grid[y+1][x]    !=    '%'    and    y    <    r-1):
            successors.append((x,y+1));
    return    successors;

def isGoalState(state):
    (x,y) = state
    return (x == food_c and y == food_r)

def nextMove( r, c, pacman_r, pacman_c, food_r, food_c, grid):
    path = []
    mark = []
    x = pacman_c
    y = pacman_r
    state = (x,y)
    explored = []
    mark.append(state)
    path.append(state)
    fringe = Queue()
    fringe.push((state,path))
    while(not isGoalState(state)):
        succs = getSuccessors(state)
        if (len(succs) > 0):
            for succ in succs:
                childPath = list(path)
                if succ not in mark:
                    childPath.append(succ)
                    mark.append(succ)
                    fringe.push((succ,childPath))
        else:
            break
        (state,path) = fringe.pop()
        explored.append(state)
        
    print len(explored)
    for (x,y) in explored:
        print y,x
    print len(path) - 1
    for (x,y) in path:
        print y,x
    return
pacman_r, pacman_c = [ int(i) for i in raw_input().strip().split() ]
food_r, food_c = [ int(i) for i in raw_input().strip().split() ]
r,c = [ int(i) for i in raw_input().strip().split() ]

grid = []
for i in xrange(0, r):
    grid.append(raw_input().strip())

nextMove(r, c, pacman_r, pacman_c, food_r, food_c, grid)

