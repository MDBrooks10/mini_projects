#TicTacToe!
#code along project from https://www.youtube.com/watch?v=kojoQkZ8LfA

def main():
    grid = [[" "," "," "],
            [" "," "," "],
            [" "," "," "]]

    player1 = "X"
    player2 = "O"

    gameOver = False

    while gameOver == False:
        #player 1

        printGrid(grid[0],grid[1],grid[2])
        grid = turn(player1, grid)
        gameOver = winCheck(player1, grid, gameOver)

        if gameOver == False:
            printGrid(grid[0],grid[1],grid[2])
            grid = turn(player2, grid)
            gameOver = winCheck(player2, grid, gameOver)

    printGrid(grid[0],grid[1],grid[2])
    print("Play again?")
    choice = input("1. Play again\n2. EXIT")

    while choice != "1" and choice != "2":
        print("Only press 1 or 2")
        choice = input("1. Play again\n2. EXIT")

    if choice == "1":
        main()

    else:
        exit()


def printGrid(r1, r2, r3):
    print(r1[0],"|",r1[1],"|",r1[2])
    print("----------")
    print(r2[0],"|",r2[1],"|",r2[2])
    print("----------")
    print(r3[0],"|",r3[1],"|",r3[2])
    print("----------")


def turn(player, grid):

    choice = 0

    while choice != " ":

        print(player,"Player Turn .....")
        row = input("choose a row: \n1. Top \n2. Middle \n3. Bottom \n")
        while row != "1" and row != "2" and row != "3":
            print("Only type 1, 2 or 3")
            row = input("choose a row: \n1. Top \n2. Middle \n3. Bottom \n")

        column = input("choose a row: \n1. Left \n2. Middle \n3. Right \n")
        while column != "1" and column != "2" and column != "3":
            print("Only type 1, 2 or 3")
            column = input("choose a row: \n1. Left \n2. Middle \n3. Right \n")


        choice = grid[int(row)-1][int(column)-1]

        if choice != " ":
            print("There is already value in that cell, try again...")

        else:
            print("Updating grid...")
            grid[int(row)-1][int(column)-1] = player
            return grid


def winCheck(player, grid, gameOver):
    #Check rows

    #top row
    if grid[0][0] == player and grid [0][1] == player and grid[0][2] == player:
        print("Top Row Win.....")
        print(player, "is the WINNER!")
        gameOver = True

    #middle row
    elif grid[1][0] == player and grid [1][1] == player and grid[1][2] == player:
        print("Middle Row Win.....")
        print(player, "is the WINNER!")
        gameOver = True

    #Bottom row
    elif grid[2][0] == player and grid [2][1] == player and grid[2][2] == player:
        print("Bottom Row Win.....")
        print(player, "is the WINNER!")
        gameOver = True

    #Check columns

    #Left column
    elif grid[0][0] == player and grid [1][0] == player and grid[2][0] == player:
        print("Left column Win.....")
        print(player, "is the WINNER!")
        gameOver = True

    #Middle column
    elif grid[0][1] == player and grid [1][1] == player and grid[2][1] == player:
        print("Middle column Win.....")
        print(player, "is the WINNER!")
        gameOver = True

    #Right column
    elif grid[0][2] == player and grid [1][2] == player and grid[2][2] == player:
        print("Right column Win.....")
        print(player, "is the WINNER!")
        gameOver = True

    #Diagonals
    elif grid[0][0] == player and grid [1][1] == player and grid[2][2] == player:
        print("Diagonal Win.....")
        print(player, "is the WINNER!")
        gameOver = True

    elif grid[0][2] == player and grid [1][1] == player and grid[2][0] == player:
        print("Diagonal Win.....")
        print(player, "is the WINNER!")
        gameOver = True

    else:
        print("No winner yet")

    spaceRemain = False

    for x in range (0, len(grid)):
        if " " in grid[x]:
            spaceRemain = True

    if spaceRemain == False:
        if gameOver == False:
            print("It's a draw")
            gameOver = True

    return gameOver

main()
