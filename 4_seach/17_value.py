# ----------
# User Instructions:
# 
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal. 
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------
from collections import deque
grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def compute_value(grid,goal,cost):
    # ----------------------------------------
    # insert code below
    # ----------------------------------------
    q = deque()
    v = 0
    visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
    visited[goal[0]][goal[1]] = True
    value = [[99 for i in range(len(grid[0]))] for j in range(len(grid))]
    value[goal[0]][goal[1]] = v
    q.append((goal[0], goal[1], v))
    while(q):
        
        x, y, v = q.popleft()
        v += cost
        for i in range(len(delta)):
            x2 = x + delta[i][0]
            y2 = y + delta[i][1]
            # print(x2,y2,v,q)
            if (x2>=0 and x2<len(grid) and y2>=0 and y2<len(grid[0])):
                # print(q,x2,y2)
                if(visited[x2][y2]==False and grid[x2][y2]==0):
                    q.append((x2, y2, v))
                    value[x2][y2] = v
                    visited[x2][y2]=True
                    # print(q)
    
    # make sure your function returns a grid of values as 
    # demonstrated in the previous video.
    return value 
print(compute_value(grid,goal,cost))