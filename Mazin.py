import random

maze = [
    list("#.....p..#"),
    list("#........#"),
    list("#........#"),
    list("#..g...###"),
    list("#......###")]

def print_maze(maze):
    for row in maze:
        print("".join(row))

def find_player(maze: list):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == "p":
                return i,j



def Movement(maze: list, move: str)-> bool :
    x, y = find_player(maze)
    nx, ny = 0, 0
    match move:
        case "w":
            nx = -1
        case "s":
            nx = 1
        case "a":
            ny = -1
        case "d":
            ny = 1
    nxf, nyf = nx+x, ny+y
    if maze[nxf][nyf] != "#":
        if maze[nxf][nyf] == "g":
            return True
        maze[nxf][nyf] = "p"
        maze[x][y] = "."
    else:
        print("opps hit a wall")
    return False

def glitch_maze(maze: list)-> bool:
    for row in range(1, len(maze) -1):
        for col in range(1, len(maze) -1):
            if maze[row][col] == "." and random.random() < 0.5:
                maze[row][col] = "#"
            if maze[row][col] == "#" and random.random() < 0.5:
                maze[row][col] = "."

while True:
    #add a if that only runs 1 time 
    print_maze(maze)
    move = input("move")
    win = Movement(maze, move)
    if move == "qq":
        break
    if win:
        print("you won")
        quit = input("press q to quit or any key to play again")
        if quit == "q":
            break
        else:
            continue




