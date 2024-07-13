"""
本题用到了贪心算法:
为了充分发挥GPU算力&#xff0c;需要尽可能多的将任务交给GPU执行&#xff0c;现在有一个任务数组&#xff0c;数组元素表示在这1秒内新增的任务个数且每秒都有新增任务。<br /> 
假设GPU最多一次执行n个任务&#xff0c;一次执行耗时1秒&#xff0c;在保证GPU不空闲情况下&#xff0c;最少需要多长时间执行完成。</p> 
输入描述: 第一个参数为GPU一次最多执行的任务个数, 取值范围[1, 10000]; 第二个参数为任务数组长度, 取值范围[1, 10000]; 第三个参数为任务数组, 数字范围[1, 10000] 
输出描述: 执行完所有任务最少需要多少秒.
用例
3
5
1 2 3 4 5
输出	
6

https://blog.csdn.net/wtswts1232/article/details/139579327
"""


import sys
lines = []
while True:
    line = sys.stdin.readline().strip()
    if line == "": break
    lines.append(line)


size, tasks, taskLst = int(lines[0]), int(lines[1]), list(int(x) for x in lines[2].split())
def process_tasks(size, tasks, taskLst):
    taskRemainLst = []
    c1, taskRemain = 0, 0
    while ((c1 < tasks) or (taskRemain > 0)):
        try: taskRemain = taskRemain + taskLst[c1]
        except: pass
        taskRemain = 0 if (taskRemain < size) else (taskRemain - size)
        print(c1, taskRemain)
        c1 = c1 + 1
    return c1

process_tasks(size, tasks, taskLst)
print("The result is: ", c1)