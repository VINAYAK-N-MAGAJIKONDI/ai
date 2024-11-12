from collections import deque

class PuzzleSolver:
    def solve(self, board):
        # Flatten the board into a tuple for easier comparison and hashing
        start_state = tuple([tile for row in board for tile in row])
        goal_state = (0, 1, 2, 3, 4, 5, 6, 7, 8)

        # If the board is already solved
        if start_state == goal_state:
            print("The board is already solved.")
            return 0

        # BFS setup
        queue = deque([(start_state, 0)])  # (state, move_count)
        visited = {start_state}  # To keep track of visited states
        parent_map = {start_state: None}  # To trace the path

        # Directions for moving the '0' (empty space)
        moves = {
            0: [1, 3], 1: [0, 2, 4], 2: [1, 5],
            3: [0, 4, 6], 4: [1, 3, 5, 7], 
            5: [2, 4, 8], 6: [3, 7], 7: [4, 6, 8], 
            8: [5, 7]
        }

        while queue:
            current_state, move_count = queue.popleft()

            # If we reached the goal state, reconstruct the path
            if current_state == goal_state:
                self.print_solution(parent_map, current_state)
                return move_count

            # Find the possible next moves (states)
            pos_0 = current_state.index(0)
            for new_pos in moves[pos_0]:
                # Create the new state by swapping the 0 tile with the adjacent tile
                new_state = list(current_state)
                new_state[pos_0], new_state[new_pos] = new_state[new_pos], new_state[pos_0]
                new_state_tuple = tuple(new_state)

                if new_state_tuple not in visited:
                    visited.add(new_state_tuple)
                    parent_map[new_state_tuple] = current_state
                    queue.append((new_state_tuple, move_count + 1))

        print("No solution found.")
        return -1  # If no solution is found

    def print_solution(self, parent_map, state):
        # Reconstruct the sequence of moves
        moves = []
        while state is not None:
            moves.append(state)
            state = parent_map[state]

        # Reverse the sequence to show from start to goal
        moves.reverse()

        # Print the board for each move in the sequence
        for idx, move in enumerate(moves):
            print(f"Move {idx}:")
            self.print_board(move)

    def print_board(self, state):
        # Print the board in a 3x3 format
        print(f"{state[0]} {state[1]} {state[2]}")
        print(f"{state[3]} {state[4]} {state[5]}")
        print(f"{state[6]} {state[7]} {state[8]}")
        print()  # Add an empty line between boards

# Test the solver
puzzle = PuzzleSolver()
initial_board = [[3, 1, 2], [4, 7, 5], [6, 8, 0]]
print("Solution path:")
moves = puzzle.solve(initial_board)
