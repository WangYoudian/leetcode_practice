#
# @lc app=leetcode.cn id=802 lang=python3
#
# [802] 找到最终的安全状态
# 分析：这题的示例给的太过简单了，容易误解成安全节点只包含终端节点和直接指向终端节点的点
#   实际上，涉及的问题是：图中环的检测（且提示中也说到了包含自环）
#   若节点出发的所有路径都不会进入环，那么这个节点就是安全节点
#   使用 BFS 和一种称作三色标记法（ Python 垃圾回收中的标记清除就是这个思路）来解决

# @lc code=start
from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        # star: ※※※  三色标记法（0：白；1：灰；2：黑）
        # 0 表示未被访问过； 1 表示访问过但是不确定是否在环中； 2 表示访问过且确定不在环中，为安全节点
        color = [0] * n

        def safe(x):
            # 已经访问过，能够知道是否成环。状态 2 将从终端节点向第一层指向它的安全节点扩散
            if color[x] > 0:
                return color[x] == 2
            # 标记为访问
            color[x] = 1
            for y in graph[x]:
                if not safe(y):
                    return False
            color[x] = 2
            return True

        return [i for i in range(n) if safe(i)]

# @lc code=end
