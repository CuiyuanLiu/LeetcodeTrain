"""
连接器:

"""

import sys
lines = []
for a in sys.stdin:
    lines.append(a.split())
    if (a == "\n"): break

lines = [
    "REQUEST=10",
    "REQUEST=30",
    "RELEASE=0",
    "REQUEST=20",
    "REQUEST=35",
    "REQUEST=10"
]

class MEMORY():
    def __init__(self):
        self.mLST = [0 for t in range(100)]
        self.currStartLoc = 0
        self.entryLst = []
    
    def checkSpare(self, start, end):
        c = start
        if (end > 100): return False
        while (c < end):
            if (self.mLST[c] != 0): return False
            c = c + 1
        return True

    def classfy(self, line):
        Type = line[0]
        digit = int(line[1])

        if (Type == "REQUEST"):
            cStartLoc = self.currStartLoc
            REPEAT = True
            while (self.checkSpare(cStartLoc, cStartLoc + digit) == False):
                if (cStartLoc + digit >= 100):
                    if (REPEAT == True): 
                        cStartLoc = 0
                        REPEAT = False
                    else:
                        break
                else:
                    cStartLoc = cStartLoc + 1

            if ((cStartLoc >= 0) and (cStartLoc + digit < 100)):
                for c in range(cStartLoc, cStartLoc + digit):
                    self.mLST[c] = 1
                self.entryLst.append((cStartLoc, digit))
            
            cStartLoc = cStartLoc + digit
            self.currStartLoc = cStartLoc
        
        elif (Type == "RELEASE"):
            cStartLoc = digit
            c = cStartLoc
            c_end = cStartLoc

            for entry in self.entryLst:
                if (cStartLoc == entry[0]): 
                    c_end = entry[0] + entry[1]

            while ((self.mLST[c] != 0) and (c < c_end)):
                self.mLST[c] = 0
                c = c + 1
        
    def run(self, lines):
        for l in lines:
            line = l.split("=") 
            self.classfy(line)
            if ("REQUEST" in line): print(self.currStartLoc)
            print(self.mLST)
    

myMEMORY = MEMORY()
myMEMORY.run(lines)
            

