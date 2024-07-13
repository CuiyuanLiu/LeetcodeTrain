import sys

lines = []
for line in sys.stdin:
    a = line.split()
    lines.append(a)

class Soduku():
    def __init__(self):
        self.rows = list(list(0 for i in range(9)) for j in range(9))
    
    def isValue(self, x, y):
        # Check if there is some value in the same row has the identical value.
        for i in range(9):
            if (i != x) and (self.rows[i][y] == self.rows[x][y]):
                return False
        
        # Check if there is some value in the same column has the identical value.
        for j in range(9):
            if (j != y) and (self.rows[x][j] == self.rows[x][y]):
                return False
        
        bx, by = int(x / 3) * 3, int(y / 3) * 3
        for i in range(bx, bx + 3):
            for j in range(by, by + 3):
                if (self.rows[i][j] == self.rows[x][y]):
                    if (not (i == x and j == y)): 
                        return False
        
        return True
    
    def DFS(self):
        for i in range(9):
            for j in range(9):
                if (self.rows[i][j] == 0):
                    for k in "123456789":
                        self.rows[i][j] = int(k)
                        if (self.isValue(i, j) and self.DFS()):
                            return True
                        else:
                            self.rows[i][j] = 0
                    return False
        return True
    
    def run(self, lines):
        c = 0
        for line in lines:
            for cj in range(9): 
                self.rows[c][cj] = int(line[cj])
            c = c + 1
        self.DFS()
        for row in self.rows:
            print(" ".join(list(str(x) for x in row)))

mySoduku = Soduku()
mySoduku.run(lines)