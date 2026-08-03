scores = {'X': 1, 'O': -1, 'Draw': 0}

def minimax(depth, isMax):
    if depth == 0:
        return 0
    if isMax:
        return max(minimax(depth-1, False), 1)
    else:
        return min(minimax(depth-1, True), -1)

print("Best Score:", minimax(3, True))