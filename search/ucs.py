import heapq
class PriorityQueue:
    def __init__(self):
        self.heap = []
    def push(self,item,priority):
        pair = (priority, item)
        heapq.heappush(self.heap, pair)
    def pop(self):
        (priority, item) =  heapq.heappop(self.heap)
        return (item,priority)
    def isEmpty(self):
        return len(self.heap) == 0

def isGoalState(state):
    (x,y) = state
    return (x == food_c and y == food_r)

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

def getCost(path, oldCost):
    newPath = list(path)
    (x,y) = newPath.pop()
    if (grid[y][x] == '.'):
        return oldCost
    return oldCost + 1
        
def nextMove( r, c, pacman_r, pacman_c, food_r, food_c, grid):
    x = pacman_c
    y = pacman_r
    state = (x,y)
    path = []
    marked = []
    explored = []
    fringe = PriorityQueue()
    oldCost = 0
    marked.append(state)
    path.append(state)
    fringe.push((state,path),0)
    while (not isGoalState(state)):
        succs = getSuccessors(state)
        explored.append(state)
        if (len(succs) > 0):
            for succ in succs:
                childPath = list(path)
                if (succ not in marked):
                    childPath.append(succ)
                    marked.append(succ)
                    cost = getCost(childPath, oldCost)
                    fringe.push((succ,childPath),cost)
        else :
            break
        ((state,path),oldCost) = fringe.pop()
    explored.append(state)
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

