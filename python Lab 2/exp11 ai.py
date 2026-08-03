states = ['A', 'B', 'C', 'D']
neighbors = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}
colors = ['Red', 'Green', 'Blue']
result = {}

def solve(state):
    if state == len(states):
        return True
    s = states[state]
    for color in colors:
        if all(result.get(n) != color for n in neighbors[s]):
            result[s] = color
            if solve(state + 1):
                return True
            del result[s]
    return False

solve(0)
print(result)