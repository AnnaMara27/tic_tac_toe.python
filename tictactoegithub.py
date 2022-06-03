grid = list("         ")
rows = [[grid[0], grid[1], grid[2]], [grid[3], grid[4], grid[5]], [grid[6], grid[7], grid[8]]]

def printGrid():
    print("-" * 9)
    print(f"| {grid[0]} {grid[1]} {grid[2]} |")
    print(f"| {grid[3]} {grid[4]} {grid[5]} |")
    print(f"| {grid[6]} {grid[7]} {grid[8]} |")
    print("-" * 9)

def getResult():
    vertical_1 = "".join([grid[0], grid[3], grid[6]])
    vertical_2 = "".join([grid[1], grid[4], grid[7]])
    vertical_3 = "".join([grid[2], grid[5], grid[8]])
    diag_1 = "".join([grid[0], grid[4],grid[8]])
    diag_2 = "".join([grid[2], grid[4],grid[6]])
    lines = [grid[0:3], grid[3:6], grid[6:9], vertical_1, vertical_2, vertical_3, diag_1, diag_2]

    if grid.count("X") - grid.count("O") >= 2 or grid.count("O") - grid.count("X") >= 2:
        return "Impossible"
    elif "XXX" in lines and "OOO" in lines:
        return "Impossible"
    elif ("XXX" not in lines and "OOO" not in lines) and (grid.count(" ") != 0 or grid.count("_") != 0):
        return "Game not finished"
    elif ("XXX" not in lines and "OOO" not in lines) and (grid.count(" ") == 0 or grid.count("_") == 0):
        return "Draw"
    elif "XXX" in lines:
        return "X wins"
    elif "OOO" in lines:
        return "O wins"
    
def checkMove(row, column):
    if row.isdigit() == False or column.isdigit() == False:
        print("You should enter numbers!")
    elif row not in ["1", "2", "3"] or column not in ["1", "2", "3"]:
        print("Coordinates should be from 1 to 3!")
    else:
        return True
        
def checkCell(x):
    if x != " " and x != "_":
        print("This cell is occupied! Choose another one!")
    else:
        return True

def updateGrid(symbol):
    rows[int(row) - 1][int(column) - 1] = symbol
    return rows

printGrid()
print("""X and O play turn by turn. X begins the game.
Please enter the coordinates of where you want to place your symbol.
The coordinates should be separated by a space.""")

while True:
    row, column = input("Please enter the coordinates for X\n>").split(" ")
    if checkMove(row, column) == True:
        if checkCell(rows[int(row) - 1][int(column) - 1]) == True:
            updateGrid("X")
            row_1 = "".join(rows[0])
            row_2 = "".join(rows[1])
            row_3 = "".join(rows[2])
            grid = row_1 + row_2 + row_3
            printGrid()
            if getResult() == "Draw":
                print(getResult())
                break
            elif getResult() == "X wins":
                print(getResult())
                break
            elif getResult() == "O wins":
                print(getResult())
                break
            else:
                row, column = input("Please enter the coordinates for O\n>").split(" ")
                if checkMove(row, column) == True:
                    if checkCell(rows[int(row) - 1][int(column) - 1]) == True:
                        updateGrid("O")
                        row_1 = "".join(rows[0])
                        row_2 = "".join(rows[1])
                        row_3 = "".join(rows[2])
                        grid = row_1 + row_2 + row_3
                        printGrid()
                        if getResult() == "Draw":
                            print(getResult())
                            break
                        elif getResult() == "X wins":
                            print(getResult())
                            break
                        elif getResult() == "O wins":
                            print(getResult())
                        else:
                            continue
            

    