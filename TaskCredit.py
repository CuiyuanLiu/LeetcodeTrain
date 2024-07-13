import sys

lines = []
for a in sys.stdin:
    if (a != "\n"): lines.append(a.split())
    else: break

print(lines)
N = int(lines[0][0])
currDiskLst = []
for line in lines[1:]:
    currLst = line
    currDiskLst.append((int(currLst[0]), int(currLst[1])))

n = len(currDiskLst)
for i in range(n - 1):
    for j in range(n - i - 1):
        if (currDiskLst[j][0] > currDiskLst[j + 1][0]):
            currDiskLst[j], currDiskLst[j + 1] = currDiskLst[j + 1], currDiskLst[j]

result = 0
time = 0
pq = []
for currDisk in currDiskLst:
    # 在当前SLA的情形下加入最大值, 并记忆当下最大值进入pq序列中
    if (currDisk[0] > time):
        pq.append(currDisk)
        sorted(pq, key = lambda x: x[1])
        result += currDisk[1]
        time = time + 1
    
    # 如果发现有更优的情况, 掉头回来修正
    else:
        if ((len(pq) > 0) and (pq[0][1] < currDisk[1])):
            result -= pq[0][1]
            pq = pq[1:]
            pq.append(currDisk)
            sorted(pq, key = lambda x: x[1])
            result += currDisk[1]

while (time > N):
    result -= pq[0]
    time -= 1
print(result)



