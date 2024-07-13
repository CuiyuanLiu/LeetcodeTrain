"""
生成哈夫曼树：
1. 给定长度为 n 的无序的数字数组, 每个数字代表二叉树的叶子节点的权值, 数字数组的值均大于等于1。
2. 完成一个函数, 根据输入的数字数组, 生成哈夫曼树, 并将哈夫曼树按照中序遍历输出。
3. 左node的权值小于等于右node的权值, root为左右节点的权值之和。当左右权值相同的时候, 左子树的高度小于右子树的高度。

解题思路： 
读取数字数组的长度和具体数值, 然后利用输入的数组构建哈夫曼树, 并对构建好的哈夫曼树进行中序遍历, 最后将结果输出。
- 定义哈夫曼树的节点类
- 构建哈夫曼树

import pandas as pd

f = open("contents.txt", "r")
ResultLst = []
for x in f: 
    ResultLst.append(x.split("&&"))
print(len(ResultLst))
df1 = pd.DataFrame(ResultLst)
df1.to_csv("Result.csv")
"""

class HNode():
    def __init__(self):
        self.weight = 0
        self.height = 1
        self.leftNode = None
        self.rightNode = None

    def setup_HNode(self, weight):
        self.weight = weight
        return self

class Htree():
    def __init__(self):
        self.root = None
        self.resultLst = []
        self.WPL = 0
    
    def constructNtree(self, HNode1: HNode, HNode2: HNode):
        newNode = HNode().setup_HNode(weight = 0)
        try:
            newNode.height += max(HNode1.height, HNode2.height)
            if (HNode1.weight < HNode2.weight):
                newNode.leftNode  = HNode1
                newNode.rightNode = HNode2
            elif ((HNode1.weight == HNode2.weight) and (HNode1.height < HNode2.height)):
                newNode.leftNode  = HNode1
                newNode.rightNode = HNode2
            else:
                newNode.leftNode  = HNode2
                newNode.rightNode = HNode1
            newNode.weight = HNode1.weight + HNode2.weight
        except: 
            pass
        return newNode
    
    def sortNodeLst(self, resultLst):
        n = len(resultLst)
        try:
            c1 = 0
            while (c1 < n - 1):
                c2 = 0
                swapped = False
                while (c2 < n - 1 - c1):
                    if (resultLst[c2].weight > resultLst[c2 + 1].weight):
                        swapped = True
                        resultLst[c2], resultLst[c2 + 1] = resultLst[c2 + 1], resultLst[c2]
                    c2 = c2 + 1
                if (not swapped): return resultLst
                c1 = c1 + 1
        except Exception as err:
            print(err)
        return resultLst

    def constructHtree(self, iptLst):
        # Constructs HuffNode for every values input.
        nodeLst = []
        sorted(iptLst)
        for v in iptLst:
            newNode = HNode().setup_HNode(weight = v)
            nodeLst.append(newNode)
        
        # Build new nodes and adding, delete originals in queue.
        try:
            newNode = nodeLst[0]
            while (len(nodeLst) > 1):
                self.sortNodeLst(nodeLst)
                # for node in nodeLst: print("Node: ", node.weight, len(nodeLst))
                newNode = self.constructNtree(nodeLst[0], nodeLst[1])
                nodeLst = nodeLst[2:]
                nodeLst.append(newNode)
                
            self.root = newNode
        except Exception as err:
            print(err)
            pass
    
    def tranverseHtree(self, currNode):
        if (currNode != None): 
            if (currNode.leftNode != None):  self.tranverseHtree(currNode.leftNode)
            self.resultLst.append(currNode.weight)
            if (currNode.rightNode != None): self.tranverseHtree(currNode.rightNode)
        else:
            pass
    
    def resetHeight(self, currNode):
        try:
            if (currNode.leftNode != None):  
                currNode.leftNode.height = currNode.height + 1
                self.resetHeight(currNode.leftNode)
            if (currNode.rightNode != None): 
                currNode.rightNode.height = currNode.height + 1
                self.resetHeight(currNode.rightNode)
        except Exception as err:
            print(err)
    
    def calculateWPL(self, currNode):
        try:
            distance = currNode.height - self.root.height
            self.WPL += currNode.weight * distance
            if (currNode.leftNode != None):  self.calculateWPL(currNode.leftNode)
            if (currNode.rightNode != None): self.calculateWPL(currNode.rightNode)
        except Exception as err:
            self.WPL += 0
    
    def run(self):
        self.root.height = 1
        self.WPL = 0
        self.resetHeight(self.root)
        self.tranverseHtree(self.root)
        self.calculateWPL(self.root)
        print("The Huffman tree is: ", self.resultLst)
        print("WPL is: ", self.WPL)


import sys
lines = []
while True:
    line = sys.stdin.readline().strip()
    if line == "": break
    lines.append(line)
nodeSize = lines[0]
nodeLst = list(int(x) for x in lines[1].split())
myTree = Htree()
myTree.constructHtree(iptLst = nodeLst)
myTree.run()
    
    