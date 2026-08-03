def alphabeta(depth, alpha, beta, maximizing):
    if depth == 0:
        return 3

    if maximizing:
        value = max(alpha, 3)
        alpha = max(alpha, value)
        return alpha
    else:
        value = min(beta, 3)
        beta = min(beta, value)
        return beta

print(alphabeta(1, -999, 999, True))