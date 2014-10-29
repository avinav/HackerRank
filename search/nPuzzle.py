from util import PriorityQueue
import timeit

class Actions:
    def __init__(self):
        self.dict = {};
    def __init__(self,state):
        (self.x,self.y) = state
        self.dict = {'LEFT':(self.x-1, self.y),'RIGHT':(self.x+1, self.y),
                     'UP':(self.x,self.y+1),'DOWN':(self.x,self.y-1)};
    def __getattr__(self, attr):
        return self.dict[attr];
    def setState(self,state):
        self.__init__(state)

def getSuccessors(state):
    (gridState,zeroPos) = state
    newGridState = [x[:] for x in gridState];
    (x,y) = zeroPos
    successors = []
    if (x >= 0 and x < c and y >= 0 and y < r):
        if(y-1 >= 0):
            newGridState = [xx[:] for xx in gridState]; 
            newGridState[y][x] = newGridState[y-1][x]
            newGridState[y-1][x] = 0 
            newState = (newGridState,(x,y-1))
            successors.append(('UP',newState))
        if(x+1 < c):
            newGridState = [xx[:] for xx in gridState];
            newGridState[y][x] = newGridState[y][x+1]
            newGridState[y][x+1] = 0 
            newState = (newGridState,(x+1,y))
            successors.append(('LEFT',newState))
        if (x-1 >= 0):
            newGridState = [xx[:] for xx in gridState];
            newGridState[y][x] = newGridState[y][x-1]
            newGridState[y][x-1] = 0 
            newState = (newGridState,(x-1,y))
            successors.append(('RIGHT',newState))
        if(y+1 < r):
            newGridState = [xx[:] for xx in gridState];
            newGridState[y][x] = newGridState[y+1][x]
            newGridState[y+1][x] = 0 
            newState = (newGridState,(x,y+1))
            successors.append(('DOWN',newState))
    return successors;

def isGoalState(state):
    sum = 0
    (gridState, zeroPos) = state
    for i in xrange(0,r):
        for j in xrange(0,c):
           sum = sum + abs(goalState[i][j] - gridState[i][j]) 
    return sum == 0

def getHeuristic(state):
    sum = 0
    (gridState,zeroPos) = state
    for i in xrange(0,r):
        for j in xrange(0,c):
            ii = (gridState[i][j]/c);
            jj = (gridState[i][j]%c);
            sum = sum + abs(ii - i) + abs(jj - j); 
    return sum

def getCost(state,oldCost):
    if (isGoalState(state)):
        return oldCost
    return oldCost + 1

def inMarked(state,marked):
    (gridState,zeroPos) = state;
    for k in xrange(0,len(marked)):
        (markedState,markedZeroPos) = marked[k];
        matched = True;
        for i in xrange(0,r):
            for j in xrange(0,c):
                if (markedState[i][j] != gridState[i][j]):
                    matched = False;
                    break;
            if(not matched):
                break;
        if (matched):
            return True;
    return False;

def nextMove(initState):
    path = [];
    marked = [];
    fringe = PriorityQueue();
    state = initState;
    (gridState,zeroPos) = state
    oldCost = 0
    fringe.push((path,state),oldCost);
    marked.append(state)
    while(not isGoalState(state)):
        succs = getSuccessors(state);
        if (len(succs) > 0):
            for succ in succs:
                childPath = list(path);
                (action,childState) = succ;
                if (not inMarked(childState,marked)):
                    childPath.append(action);
                    cost = getCost(state,oldCost) + getHeuristic(childState);
                    fringe.push((childPath,childState),cost);
                    marked.append(childState);
        else:
            break;
        ((path,state),oldCost) = fringe.pop();
    for i in xrange(0,len(path)):
        print path[i]
    
    return

m = int(raw_input().strip())
grid = []
cols = []
zeroPos = (0,0)
for i in xrange(0, m):
    cols = []
    for j in xrange(0, m):
        cols.append(int(raw_input().strip()))
        if (cols[j] == 0):
            zeroPos = (j,i)
    grid.append(cols)

r = len(grid);
c = len(grid[0]);
tempGoalState = [];
for i in xrange(0,r):
    tempGoalState = tempGoalState + grid[i];
tempGoalState.sort();

tempList = []
goalState = [];
for i in xrange(0,r*c):
    tempList.append(tempGoalState[i])
    if((i+1)%c == 0):
        goalState.append(tempList);
        tempList = []
state = (grid,zeroPos)
startTime = timeit.default_timer();
nextMove(state)
stopTime = timeit.default_timer();
print stopTime - startTime;

