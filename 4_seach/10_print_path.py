# -----------
# User Instructions:
#
# Modify the the search function so that it returns
# a shortest path as follows:
# 
# [['>', 'v', ' ', ' ', ' ', ' '],
#  [' ', '>', '>', '>', '>', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', '*']]
#
# Where '>', '<', '^', and 'v' refer to right, left, 
# up, and down motions. Note that the 'v' should be 
# lowercase. '*' should mark the goal cell.
#
# You may assume that all test cases for this function
# will have a path from init to goal.
# ----------

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    # ----------------------------------------
    # modify code below
    # ----------------------------------------
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed[init[0]][init[1]] = 1
    ## curr_path = [[' ' for i in range(len(grid[0]))] for j in range(len(grid))]
    ## print(curr_path)

    x = init[0]
    y = init[1]
    g = 0
    path = list()
    open = [[g, x, y, []]]

    found = False  # flag that is set when search is complete
    resign = False # flag set if we can't find expand

    while not found and not resign:
        if len(open) == 0:
            resign = True
            return 'fail'
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            x = next[1]
            y = next[2]
            g = next[0]
            path = next[3]
            #print(path)
            #print(x,y,g,path)

            if x == goal[0] and y == goal[1]:
                found = True
                ##path[x][y] = '*'
                ##final_path = [[' ' for i in range(len(grid[0]))] for j in range(len(grid))]
                final_path = [[' ' for i in range(len(grid[0]))] for j in range(len(grid))]
                final_path[goal[0]][goal[1]] = '*'
                x = init[0]
                y = init[1]
                for i in range(len(path)):
                    ##print(final_path)
                    final_path[x][y] = path[i]
                    if(path[i]=='<'):
                        y-=1
                    elif(path[i]=='>'):
                        y+=1
                    elif(path[i]=='^'):
                        x-=1
                    elif(path[i]=='v'):
                        x+=1
                return final_path
                    
                
                ##nprint(path)
                    
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            ##new_path = path
                            ##path[x][y] = delta_name[i]
                            ##print(new_path)
                            new_path=path[:]
                            new_path.append(delta_name[i])
                            ##print( delta_name[i])
                            open.append([g2, x2, y2, new_path])
                            closed[x2][y2] = 1

    return path # make sure you return the shortest path
print(search(grid,init,goal,cost))
