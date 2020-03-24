import copy
from priorityqueue import PriorityQueue
class Puzzle:
    # Constructor
    def __init__(self, path):
        # Define board and size
        self.board = []
        self.n = 0

        f = open(path, "r")
        for line in f:
            self.board.append(list(map(lambda x : int(x), line.split())))
        
        self.n = len(self.board)

    # Find empty cell position
    # Returns : (row, colunn)
    def find_empty(self):
        for i,row in enumerate(self.board):
            for j,value in enumerate(row):
                if(value==self.n**2):
                    return (i,j)

    # Move empty cell up
    def move_up(self):
        (r, c) = self.find_empty()
        if(r==0):
            raise InvalidMoveException()
        else:
            new_puzzle = copy.deepcopy(self)    
            new_puzzle.board[r][c], new_puzzle.board[r-1][c] = new_puzzle.board[r-1][c], new_puzzle.board[r][c]
            return new_puzzle 
    
    # Move empty cell down
    def move_down(self):
        (r, c) = self.find_empty()
        if(r==self.n-1):
            raise InvalidMoveException()
        else:
            new_puzzle = copy.deepcopy(self)    
            new_puzzle.board[r][c], new_puzzle.board[r+1][c] = new_puzzle.board[r+1][c], new_puzzle.board[r][c]
            return new_puzzle

    # Move empty cell left
    def move_left(self):
        (r, c) = self.find_empty()
        if(c==0):
            raise InvalidMoveException()
        else:
            new_puzzle = copy.deepcopy(self)    
            new_puzzle.board[r][c], new_puzzle.board[r][c-1] = new_puzzle.board[r][c-1], new_puzzle.board[r][c]
            return new_puzzle
    
    # Move empty cell right
    def move_right(self):
        (r, c) = self.find_empty()
        if(c==self.n-1):
            raise InvalidMoveException()
        else:
            new_puzzle = copy.deepcopy(self)    
            new_puzzle.board[r][c], new_puzzle.board[r][c+1] = new_puzzle.board[r][c+1], new_puzzle.board[r][c]
            return new_puzzle

    # Test whether the puzzle is solvable or not
    def is_solveable(self):
        (r, c) = self.find_empty()

        # Flatten board
        tmp = [self.board[i][j] for i in range(self.n) for j in range(self.n)]

        # Find empty cell offset
        x = (r+c) % 2 if (self.n % 2 == 0) else 0

        sum = 0
        for i in range(0,self.n**2):
            for j in range(i+1,self.n**2):
                if(tmp[i]>tmp[j]):
                    sum+=1

        print("Inversions:", sum)
        print("Offset:", x)

        return (sum + x) % 2 == 0

    # Output board
    def output_board(self):
        for row in self.board:
            for value in row:
                print('%4s' % (value if value!=self.n**2 else "#"), end="")
            print()

    # Create next state space
    def create_states(self):
        boards = []

        try:
            boards.append(self.move_up())
        except InvalidMoveException as e:
            boards.append(None)

        try:
            boards.append(self.move_down())
        except InvalidMoveException as e:
            boards.append(None)

        try:
            boards.append(self.move_left())
        except InvalidMoveException as e:
            boards.append(None)

        try:
            boards.append(self.move_right())
        except InvalidMoveException as e:
            boards.append(None)

        return boards

    def __check_false_tiles(self):
        result = 0
        flat = [self.board[i][j] for i in range(self.n) for j in range(self.n)]
        
        for i in range(1,(self.n**2)+1):
            if(flat[i-1]!=self.n**2 and flat[i-1] != i):
                result+=1

        return result

    def __check_final_state(self):
        flat = [self.board[i][j] for i in range(self.n) for j in range(self.n)]
        for i in range(1,(self.n**2)+1):
            if(flat[i-1] != i):
                return False

        return True

    def __convert_matrix_to_string(self):
        result = ""

        flat = [self.board[i][j] for i in range(self.n) for j in range(self.n)]
        for item in flat:
            result += "{:02d}".format(item)

        return result

    # Solve board using Branch & Bound
    def solve(self):
        root = copy.deepcopy(self)
        pq = PriorityQueue(lambda x,y : x[0] + x[1].__check_false_tiles() < y[0] + y[1].__check_false_tiles())
        # visited = {}
        found = False

        # solution = []

        pq.push((0, root))
        # visited[root.__convert_matrix_to_string()] = 1

        while(not found and not pq.is_empty()):
            current = pq.front()
            # solution.append()
            pq.pop()
            branches = current[1].create_states()
            
            print("Estimated cost:", current[0] + current[1].__check_false_tiles())
            current[1].output_board()
            # print(visited)
            print()

            for index, state in enumerate(branches):
                if(state !=None):
                    if(state.__check_final_state()):
                        state.output_board()
                        found = True
                        break
                    # elif(state.__convert_matrix_to_string() not in visited):
                    else:
                        pq.push((current[0]+1,state))
                        # visited[state.__convert_matrix_to_string()] = 1


class InvalidMoveException(Exception):
    def __init__(self, message = "Invalid move"):
        super(InvalidMoveException, self).__init__(message)