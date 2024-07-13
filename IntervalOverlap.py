"""
区间交叠/贪心算法
<p>给定坐标轴上的一组线段,线段的起点和终点均为整数并且长度不小于1,请你从中找到最少数量的线段,这些线段可以覆盖住所有线段。
输入描述:
第一行输入为所有线段的数量,不超过10000,后面每行表示一条线段,格式为”x,y”, x和y 分别表示起点和终点,取值范围是[-10^5 ,10^5]。
输出描述:
<p>最少线段数量,为正整数。输入3 1,4 2,5 3,6输出2
"""

import sys
lines = []
while True:
    line = sys.stdin.readline().strip()
    if line == "": break
    lines.append(line)

IntSize = int(lines[0])
IntLst = list([int(x.split(",")[0]), int(x.split(",")[1])] for x in lines[1:])

def FindSide(Direction, IntLst):
    Optimizer = IntLst[0]
    c, n = 0, len(IntLst)
    while (c < n):
        if (Direction == 0):   Optimizer = IntLst[c] if (Optimizer[0] > IntLst[c][0]) else Optimizer
        elif (Direction == 1): Optimizer = IntLst[c] if (Optimizer[0] < IntLst[c][0]) else Optimizer
        c = c + 1
    return Optimizer

def GreedySearch(IntLst):
    LeftInt = FindSide(0, IntLst)
    xLst = list(x[0] for x in IntLst)
    yLst = list(y[1] for y in IntLst)
    y_max = max(yLst)

    startInt = LeftInt
    count = 0
    while (startInt[1] < y_max):
        PossibleSet = []
        for y in IntLst:
            if (y[0] < startInt[1]): PossibleSet.append(y)
        currRightInt = FindSide(1, PossibleSet)
        startInt = currRightInt
        count = count + 1
    count = count + 1
    return count
    
print(GreedySearch(IntLst))
    
            