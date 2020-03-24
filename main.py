from puzzle import Puzzle
from priorityqueue import PriorityQueue
from statespacetree import StateSpaceTree

# g(i) function for checking misplaced tiles
def check_false_tiles(puzzle):
    result = 0
    flat = puzzle.flattened_board()
    
    for i in range(1, puzzle.n**2+1):
        if(flat[i-1] != i):
            result+=1

    return result

# Check whether matrix is sorted or not
def check_final_state(puzzle):
    flat = puzzle.flattened_board()
    
    for i in range(1, (puzzle.n**2)+1):
        if(flat[i-1] != i):
            return False

    return True

def generate_solution(solved_state):
    moves = ["Up", "Left", "Right", "Down"]
    solution = []
    state = solved_state.parent
    prev = solved_state

    while(state != None):
        move = ""
        
        # Find branch
        for i in range(4):
            if(state.branches[i] == prev):
                move = moves[i]
                break
        solution.insert(0, (move, prev) )

        prev = state
        state =  state.parent
        if(state != None and state.parent != None):
            state.branches =  state.parent.branches

    
    return solution

# Initiate root
root = StateSpaceTree( Puzzle("./input/1.txt") )

# Make priority queue for branching
pq = PriorityQueue(lambda x,y : x.depth + check_false_tiles(x.root) < y.depth + check_false_tiles(y.root))

# Initiate priority queue
pq.push( root )

solution_state = None

while(not pq.is_empty()):
    current = pq.front()
    pq.pop()

    # Output current processed board
    current.root.output_board()

    if(check_final_state(current.root)):
        solution_state = current
        break

    # Generate state in tree
    current.create_states()

    # Append generate states to pq
    for state in current.branches:
        if(state != None and state.root != None):
            pq.push(state)
    

solution_array = generate_solution(solution_state)

for index, (move,state) in enumerate(solution_array):
    print("Step", str(index+1) + ":", move , "-----")
    state.root.output_board()


print("Solved")