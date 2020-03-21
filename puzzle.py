class Puzzle:
    def __init__(self, path):
        self.board = []
        self.n = 0

        f = open(path, "r")
        for line in f:
            self.board.append(list(map(lambda x : int(x), line.split())))
        
        self.n = len(self.board)

    def findEmpty(self):
        for i,row in enumerate(self.board):
            for j,value in enumerate(row):
                if(value==16):
                    return (i,j)


    def moveUp(self):
        (r, c) = self.findEmpty()
        if(r==0):
            raise Exception(r,c)
        else:
            self.board[r][c], self.board[r-1][c] = self.board[r-1][c], self.board[r][c] 
    
    def moveDown(self):
        (r, c) = self.findEmpty()
        if(r==self.n-1):
            raise Exception(r,c)
        else:
            self.board[r][c], self.board[r+1][c] = self.board[r+1][c], self.board[r][c] 
    
    def moveLeft(self):
        (r, c) = self.findEmpty()
        if(c==0):
            raise Exception(r,c)
        else:
            self.board[r][c], self.board[r][c-1] = self.board[r][c-1], self.board[r][c] 
    
    def moveRight(self):
        (r, c) = self.findEmpty()
        if(c==self.n-1):
            raise Exception(r,c)
        else:
            self.board[r][c], self.board[r][c+1] = self.board[r][c+1], self.board[r][c] 

    def solveable(self):
        (r, c) = self.findEmpty()

        tmp = [self.board[i][j] for i in range(self.n) for j in range(self.n)]

        x = 0
        if(self.n % 2 == 0):
            x = (r+c) % 2

        sum = 0
        for i in range(0,self.n**2):
            for j in range(i+1,self.n**2):
                if(tmp[i]>tmp[j]):
                    sum+=1
            print("---")

        print(sum, x)

        return (sum + x) % 2 == 0

    def outputBoard(self):
        print(self.board)