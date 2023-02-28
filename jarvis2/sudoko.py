



def sudoko():
    rows, cols = (9, 9)

    arr = [[0 for i in range(cols)] for j in range(rows)]
    
    # again in this new array lets change
    # the first element of the first row
    # to 1 and print the array


    arr[0][2] =8
    arr[0][4] =6
    arr[0][5] =2

    arr[1][1] =3
    arr[1][3] =8
    arr[1][4] =4
    arr[1][6] =9
    arr[1][8] =2

    arr[2][0] =9
    arr[2][2] =6
    arr[2][7] =1
    arr[2][8] =4

    arr[3][1] =1
    arr[3][2] =2
    arr[3][5] =8
    arr[3][6] =6

    arr[4][0] =3
    arr[4][4] =7
    arr[4][5] =9
    arr[4][7] =2

    arr[5][1] =6
    arr[5][3] =1
    arr[5][7] =3
    arr[5][8] =7

    arr[6][2] =1
    arr[6][3] =7
    arr[6][4] =8
    arr[6][6] =3

    arr[7][0] =6
    arr[7][1] =8
    arr[7][2] =5
    arr[7][3] =2
    arr[7][6] =7
    arr[7][7] =4

    arr[8][0] =4
    arr[8][4] =9
    arr[8][5] =6
    arr[8][8] =1

    for row in arr:
        print(row)

    print("-------------------------------")

    temp = 1
    temp2 = 1

    
    for i in range(9):
            for r in range(9):
                for c in range(9):
                    temp2 = arr[r][c] 
                    for t in range(9):
                        if arr[r][c]!=0:
                            break
                        else:  
                            temp = arr[t][c] 
                            if temp == temp2:
                                temp2 +=1
                               
                            else:
                                temp2=temp2
                                
                            for p in range(8):
                                temp =arr[r][p]
                                if temp ==temp2:
                                    temp2 +=1
                                    
                                else:
                                    temp2=temp2
                    arr[r][c]=temp2    
    
    for row in arr:
        print(row)

sudoko()






def findNextCellToFill(grid, i, j):
        for x in range(i,9):
                for y in range(j,9):
                        if grid[x][y] == 0:
                                return x,y
        for x in range(0,9):
                for y in range(0,9):
                        if grid[x][y] == 0:
                                return x,y
        return -1,-1

def isValid(grid, i, j, e):
        rowOk = all([e != grid[i][x] for x in range(9)])
        if rowOk:
                columnOk = all([e != grid[x][j] for x in range(9)])
                if columnOk:
                        # finding the top left x,y co-ordinates of the section containing the i,j cell
                        secTopX, secTopY = 3 *(i//3), 3 *(j//3) #floored quotient should be used here. 
                        for x in range(secTopX, secTopX+3):
                                for y in range(secTopY, secTopY+3):
                                        if grid[x][y] == e:
                                                return False
                        return True
        return False

def solveSudoku(grid, i=0, j=0):
        i,j = findNextCellToFill(grid, i, j)
        if i == -1:
                return True
        for e in range(1,10):
                if isValid(grid,i,j,e):
                        grid[i][j] = e
                        if solveSudoku(grid, i, j):
                                return True
                        # Undo the current cell for backtracking
                        grid[i][j] = 0
        return False



rows, cols = (9, 9)

arr = [[0 for i in range(cols)] for j in range(rows)]
    
    # again in this new array lets change
    # the first element of the first row
    # to 1 and print the array


arr[0][2] =8
arr[0][4] =6
arr[0][5] =2

arr[1][1] =3
arr[1][3] =8
arr[1][4] =4
arr[1][6] =9
arr[1][8] =2

arr[2][0] =9
arr[2][2] =6
arr[2][7] =1
arr[2][8] =4

arr[3][1] =1
arr[3][2] =2
arr[3][5] =8
arr[3][6] =6

arr[4][0] =3
arr[4][4] =7
arr[4][5] =9
arr[4][7] =2

arr[5][1] =6
arr[5][3] =1
arr[5][7] =3
arr[5][8] =7

arr[6][2] =1
arr[6][3] =7
arr[6][4] =8
arr[6][6] =3

arr[7][0] =6
arr[7][1] =8
arr[7][2] =5
arr[7][3] =2
arr[7][6] =7
arr[7][7] =4

arr[8][0] =4
arr[8][4] =9
arr[8][5] =6
arr[8][8] =1

for row in arr:
        print(row)

print("-------------------------------")


solveSudoku(arr)

for row in arr:
        print(row)
