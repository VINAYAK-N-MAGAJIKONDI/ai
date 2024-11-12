def dfs(state, visited):
    monkey, box, banana, onbox, hasBanana = state

    # Base case: If the monkey has the banana, the goal is achieved
    if hasBanana:
        print("Monkey successfully got the banana!")
        return True

    # If this state has been visited, return False to avoid cycles
    if state in visited:
        return False
    visited.add(state)

    # Case 1: If the monkey is not on the box and is not at the box location
    if not onbox and monkey != box:
        newState = (box, box, banana, onbox, hasBanana)
        print(f"Monkey moves from {monkey} to {box}.")
        if dfs(newState, visited):
            return True

    # Case 2: If the monkey is not on the box, is at the box, and the box is not at the banana
    if not onbox and monkey == box and box != banana:
        newState = (banana, banana, banana, onbox, hasBanana)
        print(f"Monkey pushes the box from {box} to {banana}.")
        if dfs(newState, visited):
            return True

    # Case 3: If the monkey is at the box and the box is at the banana
    if not onbox and monkey == box == banana:
        newState = (monkey, box, banana, True, hasBanana)
        print("Monkey climbs on the box.")
        if dfs(newState, visited):
            return True

    # Case 4: If the monkey is on the box and the box is at the banana
    if onbox and box == banana:
        newState = (monkey, box, banana, onbox, True)
        print("Monkey grabs the banana!")
        if dfs(newState, visited):
            return True

    return False


def solve_dfs():
    initial = ('door', 'corner', 'center', False, False)
    visited = set()
    if not dfs(initial, visited):
        print("The monkey failed to get the banana.")


solve_dfs()
