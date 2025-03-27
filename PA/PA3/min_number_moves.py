def min_number_of_moves(maze):
    n = len(maze)

    if maze[0][0]==0:
        return -1

    visited = set()

    q = [(0,0,0)]

    while q:
        y, x, steps = q.pop(0)

        if (y, x) == (n-1, n-1):
            return steps

        # Read the value of the current position
        possible_move = maze[y][x]



        # # Up
        # if 0 < y - possible_move <= n-1 and (y-possible_move, x) not in visited:
        #     visited.add((y - possible_move, x))
        #     q.append((y-possible_move,x,steps+1))
        #
        # # Down
        # if 0 < y + possible_move <= n-1 and (y+possible_move, x) not in visited:
        #     visited.add((y + possible_move, x))
        #     q.append((y+possible_move,x,steps+1))
        #
        # # Left
        # if 0 < x - possible_move <= n-1 and (y, x-possible_move) not in visited:
        #     visited.add((y, x - possible_move))
        #     q.append((y,x-possible_move,steps+1))
        #
        # # Right
        # if 0 < x + possible_move <= n-1 and (y, x+possible_move) not in visited:
        #     visited.add((y, x + possible_move))
        #     q.append((y,x+possible_move,steps+1))

    return -1

maze = [[3,5,7,4,6],
        [5,3,1,5,3],
        [2,8,3,1,4],
        [4,5,7,2,3],
        [3,1,3,2,0]]

print(min_number_of_moves(maze))