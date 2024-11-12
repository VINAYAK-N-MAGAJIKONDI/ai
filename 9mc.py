from collections import deque



def is_valid_state(M_left, C_left, M_right, C_right):
   
    if M_left < 0 or C_left < 0 or M_right < 0 or C_right < 0:
        return False
    if (M_left < C_left and M_left > 0) or (M_right < C_right and M_right > 0):
        return False
    return True

def get_next_states(state):
    M_left, C_left, Boat_position = state
    M_right = 3 - M_left 
    C_right = 3 - C_left      
    next_states = []
   
    moves = [
        (1, 0), (0, 1), 
        (2, 0), (0, 2),          (1, 1)                ]
    
    for m, c in moves:
        if Boat_position == 1:            
            new_M_left = M_left - m
            new_C_left = C_left - c
            new_M_right = M_right + m
            new_C_right = C_right + c
            new_boat_position = 0
        else:  
            new_M_left = M_left + m
            new_C_left = C_left + c
            new_M_right = M_right - m
            new_C_right = C_right - c
            new_boat_position = 1
        
       
        if is_valid_state(new_M_left, new_C_left, new_M_right, new_C_right):
            next_states.append((new_M_left, new_C_left, new_boat_position))
    
    return next_states

def bfs():
    initial_state = (3, 3, 1)  
    goal_state = (0, 0, 0) 
    
   
    queue = deque([(initial_state, [])])  # Queue stores (state, path_taken_to_reach_this_state)
    visited = set([initial_state])  # Set to keep track of visited states
    
    while queue:
        state, path = queue.popleft()
        
        # If we reach the goal state, return the path
        if state == goal_state:
            return path + [state]
        
        # Get next possible states and add to the queue if not visited
        for next_state in get_next_states(state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [state]))
    
    return None  # If no solution found

def print_solution(solution):
    if solution is None:
        print("No solution found!")
    else:
        for state in solution:
            M_left, C_left, Boat_position = state
            M_right = 3 - M_left
            C_right = 3 - C_left
            boat_side = 'Left' if Boat_position == 1 else 'Right'
            print(f"Left -> M:{M_left} C:{C_left} | Boat: {boat_side} | Right -> M:{M_right} C:{C_right}")

# Run the BFS to find the solution
solution = bfs()
print_solution(solution)