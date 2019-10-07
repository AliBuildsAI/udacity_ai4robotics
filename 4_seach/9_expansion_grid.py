# -----------
# User Instructions:
# 
# Modify the function search so that it returns
# a table of values called expand. This table
# will keep track of which step each node was
# expanded.
#
# Make sure that the initial cell in the grid 
# you return has the value 0.
# ----------

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']
from collections import deque
def search(grid,init,goal,cost):
    # ----------------------------------------
    # modify code below
    # ----------------------------------------
    expand = None
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    visited = []
    expand = []
    n_row = len(grid)
    n_col = len(grid[0])
    expand = [[-1 for i in range(len(grid[0]))] for j in range(len(grid))]
    visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]

    visited[0][0]=True
    #print(visited)
    #print(expand)
    count = 0   
    q= deque()
    q.append((0,0,0))
    while(q):
        cost, row, col = q.popleft()
        #print(row,col)
        #if(visited[row][col]!=False): continue
        expand[row][col] = count
        count +=1
        #print(count)
        #print(visited)
        #print(expand)
        if(row+1<n_row and visited[row+1][col]==False and grid[row+1][col]==0):
            if(row+1 == goal[0] and col== goal[1]):
                expand[row+1][col] = count
                return expand
            q.append((cost+1,row+1,col))
            visited[row+1][col]=True
        if(row>0 and visited[row-1][col]==False and grid[row-1][col]==0):
            if(row-1 == goal[0] and col== goal[1]):
                expand[row-1][col] = count
                return expand
            q.append((cost+1,row-1,col))
            visited[row-1][col]=True

        if(col+1<n_col and visited[row][col+1]==False and grid[row][col+1]==0):
            if(row == goal[0] and col+1== goal[1]):
                expand[row][col+1]= count
                return expand       
            q.append((cost+1,row,col+1))
            visited[row][col+1]=True

        if(col>0 and visited[row][col-1]==False and grid[row][col-1]==0):
            if(row == goal[0] and col-1== goal[1]):
                expand[row][col-1] = count
                return expand        
            q.append((cost+1,row,col-1))
            visited[row][col-1]=True


    return expand