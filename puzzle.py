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
            return None
        else:
            new_puzzle = copy.deepcopy(self)    
            new_puzzle.board[r][c], new_puzzle.board[r-1][c] = new_puzzle.board[r-1][c], new_puzzle.board[r][c]
            return new_puzzle 
    
    # Move empty cell down
    def move_down(self):
        (r, c) = self.find_empty()
        if(r==self.n-1):
            return None
        else:
            new_puzzle = copy.deepcopy(self)    
            new_puzzle.board[r][c], new_puzzle.board[r+1][c] = new_puzzle.board[r+1][c], new_puzzle.board[r][c]
            return new_puzzle

    # Move empty cell left
    def move_left(self):
        (r, c) = self.find_empty()
        if(c==0):
            return None
        else:
            new_puzzle = copy.deepcopy(self)    
            new_puzzle.board[r][c], new_puzzle.board[r][c-1] = new_puzzle.board[r][c-1], new_puzzle.board[r][c]
            return new_puzzle
    
    # Move empty cell right
    def move_right(self):
        (r, c) = self.find_empty()
        if(c==self.n-1):
            return None
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

    # Return flattened board
    def flattened_board(self):
        return [val for arr in self.board for val in arr]
