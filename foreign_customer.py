"""
有位客人来自异国，该国使用m进制计数。
该客人有一个幸运数字n，在消费后总喜欢计算本次支付的花费(折算为异国的价格后)存在有多少个幸运数字
问题: 当其购买一个在我国价值为k的商品后, 其中包含多少幸运数字?

输入: 第一行输入为k n m
k 代表购买物品的价值, n 代表客人的幸运数字, m 代表客人所在国家的进制。
"""

import sys 
k, n, m = 0, 0, 0
while True:
    try: k, n, m = map(int, input().split())
    except: break

def convert(k, m):
    c1, c2, target_k, result = 0, 0, k, 0
    while (target_k > 0):
        c2 = target_k % m
        result = result + (10 ** c1) * c2 
        target_k = int(target_k / m)
        c1 = c1 + 1
    return result

result = list(int(x) for x in str(convert(k, m)))
c3 = 0
for c in result:
    if c == n: c3 = c3 + 1
print(result, c3)
 
