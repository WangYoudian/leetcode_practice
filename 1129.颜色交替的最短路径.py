#
# @lc app=leetcode.cn id=1129 lang=python3
#
# [1129] 颜色交替的最短路径
# 难点：怎么知道路径中上一个是蓝色边还是红色边呢？写两个 dfs ？
# 显然，一个图中只能写一个 dfs ，否则也会因为颜色切换脑子处理不过来
# 正确的思路是（看了题解后），以源点为例，出发有红蓝两种可能性，
# 若遇到的是中间节点，从红进入，而节点的下一个节点刚好也是红，此时，
# 可以通过边数为奇数的环进行中转，例如：蓝 - 红 - 蓝的环，回到中间节点自身，
# 那么这时它的下一跳就刚好可以进入红色边连接的节点了
# https://leetcode.cn/problems/shortest-path-with-alternating-colors/solution/by-bai-mu-ying-li-dra-eniac-jehj/

# 常规 DAG BFS 中，为了避免由于存在环导致的重复访问，采用了 visited 标记数组进行控制
# 对于这里，稍稍复杂一些，需要知道是从红色还是蓝色进入的，因此 visited 为二维数组（ n*2 规模）

# @lc code=start
import sys
from collections import defaultdict, deque
from typing import List


class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        # star: ※※※  二维的访问标记数组
        visited = [[0] * 2 for _ in range(n)]
        for src, dst in red_edges:
            graph[src].append((dst, 0))
        for src, dst in blue_edges:
            graph[src].append((dst, 1))

        # dis 表示节点是否可达
        dis = [2**31-1] * n
        dis[0] = 0
        # 从 0 出发，有两种选择的路径
        # 节点，距离，颜色
        q = deque()
        q.append((0, 0, 0))
        q.append((0, 0, 1))

        while q:
            src, distance, color = q.popleft()
            for dst, next_color in graph[src]:
                if next_color != color and visited[dst][next_color] == 0:
                    dis[dst] = min(dis[dst], distance + 1)
                    q.append((dst, distance + 1, next_color))
                    visited[dst][next_color] = 1
        # 修正 dis 并输出
        for i in range(n):
            if dis[i] == 2**31 - 1:
                dis[i] = -1
        return dis

# @lc code=end


if __name__ == '__main__':
    solution =  Solution()
    n = 3
    red = [[0, 1], [1, 2]]
    blue = []
    print(solution.shortestAlternatingPaths(n, red, blue))
