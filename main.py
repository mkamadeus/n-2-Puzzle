import time
from puzzle import Puzzle
from priorityqueue import PriorityQueue
from statespacetree import StateSpaceTree

# g(i) function for checking misplaced tiles
def check_misplaced_tiles(puzzle):
    result = 0
    flat = puzzle.flattened_board()
    
    for i in range(1, puzzle.n**2+1):
        if(flat[i-1] != i):
            result+=1

    return result

# g(i) function for checking Manhattan Distance
def check_manhattan_distance(puzzle):
    result = 0
    flat = puzzle.flattened_board()

    for index in range(0, puzzle.n**2):
        cur = flat[index]
        if(cur!=puzzle.n**2):
            cur_r, cur_c = (cur-1) // puzzle.n, (cur-1) % puzzle.n
            index_r, index_c = index // puzzle.n, index % puzzle.n

            result += abs(index_r - cur_r) + abs(index_c - cur_c)

    return result

# Check whether matrix is sorted or not
def check_final_state(puzzle):
    flat = puzzle.flattened_board()
    
    for i in range(1, (puzzle.n**2)+1):
        if(flat[i-1] != i):
            return False

    return True

# Generate solution from solved node
def generate_solution(solved_state):
    solution = []

    state = solved_state.parent
    prev = solved_state

    while(state != None):
       solution.insert(0,prev) 
       prev = state
       state = state.parent
    
    return solution

# Filename input
filename = input("Enter filename: ")

# Initiate root
root = StateSpaceTree( Puzzle("./input/" + filename) )
root.root.output_board()
print()

# Check if puzzle is solveable
if(not root.root.is_solveable()):
    print("Puzzle is unsolveable.")
    exit

print("Puzzle is solveable.")
print()

# Node generated count
node_count = 1

# Make priority queue for branching
# On priority : lowest cost with last in first
pq = PriorityQueue(lambda x,y : x.depth + check_misplaced_tiles(x.root) <= y.depth + check_misplaced_tiles(y.root))

# Initiate priority queue
pq.push(root)

# Variable to store solution state
solution_state = None

# List possible moves for puzzle
moves_units = [(-1,0), (0,-1), (1,0), (0,1)]
moves_names = ["Up", "Left", "Down", "Right"]

# Start timer
time_start = time.process_time_ns()

# Searching for solution using Branch and Bound
while(not pq.is_empty()):
    # Get front item in queue
    current = pq.front()
    pq.pop()

    # If currently checking final state, save
    if(check_final_state(current.root)):
        solution_state = current
        break

    # Append generate states to pq
    for i, (dr, dc) in enumerate(moves_units):
        if(moves_names[(i+2)%4] != current.move):
            result = StateSpaceTree(current.root.move(dr, dc), parent=current, depth=current.depth+1, move=moves_names[i])
            if(result != None and result.root != None):
                node_count += 1
                pq.push( result )

# Generate solution from result
solution_array = generate_solution(solution_state)

# Stop timer
time_stop = time.process_time_ns()

# Output solution
for index, state in enumerate(solution_array):
    print("Step", str(index+1) + ":", state.move , "-----")
    state.root.output_board()
    print()

# Output details
print("Total moves:", len(solution_array))
shorthand = ""
for i in range(len(solution_array)):
    shorthand += solution_array[i].move[0] + " "
shorthand += "Solved"
print(shorthand)

# Output nodes generated
print(node_count,"nodes generated")

# Output time
time_delta = time_stop - time_start
print(time_delta / 1000000, "ms taken")