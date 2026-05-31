import random
import os

maze = [
    list("####################"),
    list("#p.....#..........#"),
    list("#.###.#.#.######..#"),
    list("#...#.#.#......#..#"),
    list("###.#.#.######.#..#"),
    list("#...#.#......#.#..#"),
    list("#.###.######.#.#..#"),
    list("#.....#......#.#..#"),
    list("#.#####.######.#.g#"),
    list("####################")]

def clear():
    print("\n" * 50)


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
        case _:
            print("opps i don't understand")
            return False

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

def playgame():
    moves_done = 0
    while True:
        global first_time
        #add a if that only runs 1 time
        if first_time:
            print("=" * 40)
            print("        ⚡ GLITCH MAZE ⚡")
            print("=" * 40)
            print("Reach the goal (G) before the maze traps you!")
            print("Controls: w-up, s-down, d-right, a-left ")
            print("Special:The maze will GLITCH every few moves...")
            print()
            print("(type 'es' as move to exit a game) ")

            print("=" * 40)
            first_time = False
        print_maze(maze)

        move = input("move: ")
        moves_done += 1

        win = Movement(maze, move)

        if move == "es":
            break

        if moves_done%3 == 0:
            glitch_maze(maze)

        if win:
            print("you won")
            break
        clear()

first_time = True
while True:
    playgame()
    if input("play again! (y/n): ") != "y":
        break

