

from collections import deque

# Goal state
goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Initial state
start = [
    [1, 2, 3], 
    [4, 5, 0],
    [6, 7, 8]
]

moves = [(1,0), (-1,0), (0,1), (0,-1)]

# Find blank position
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def neighbours(state):
    x, y = find_blank(state)
    result = []

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
 
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            result.append(new_state)

    return result

def bfs(start, goal):
    queue = deque([(start, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path + [state]

        visited.add(tuple(map(tuple, state)))

        for next_state in neighbours(state):
            if tuple(map(tuple, next_state)) not in visited:
                queue.append((next_state, path + [state]))

    return None

solution = bfs(start, goal)

if solution:
    print("Solution Found:\n")
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No Solution" )