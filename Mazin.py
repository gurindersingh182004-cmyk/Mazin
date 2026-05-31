maze = [
    list("######p###"),
    list("#......###"),
    list("#..###.###"),
    list("#.#g##.###"),
    list("###....###")]

def print_maze(maze):
    for row in maze:
        print("".join(row))

def FindPlayer():
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == "p":
                return i,j


