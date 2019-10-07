# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

from collections import deque
grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    visited = []
    n_row = len(grid)
    n_col = len(grid[0])
    for i in range(len(grid)):
        visited.append([])
        for j in range(len(grid[0])):
            visited[-1].append(False)
    visited[0][0]=True
    q= deque()
    q.append((0,0,0))
    while(q):
        cost, row, col = q.popleft()
        visited[row][col] = True
        if(row+1<n_row and visited[row+1][col]==False and grid[row+1][col]==0):
            if(row+1 == goal[0] and col== goal[1]):
                return [cost+1,row+1,col]
            q.append((cost+1,row+1,col))
        if(row>0 and visited[row-1][col]==False and grid[row-1][col]==0):
            if(row-1 == goal[0] and col== goal[1]):
                return [cost+1,row-1,col]
            q.append((cost+1,row-1,col))
        if(col+1<n_col and visited[row][col+1]==False and grid[row][col+1]==0):
            if(row == goal[0] and col+1== goal[1]):
                return [cost+1,row,col+1]         
            q.append((cost+1,row,col+1))
        if(col>0 and visited[row][col-1]==False and grid[row][col-1]==0):
            if(row == goal[0] and col-1== goal[1]):
                return [cost+1,row,col-1]         
            q.append((cost+1,row,col-1))
                       
    
    return 'fail'