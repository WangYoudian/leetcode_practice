#
# @lc app=leetcode.cn id=329 lang=python3
#
# [329] 矩阵中的最长递增路径
#
# 总结：矩阵中搜索，四个方向可以定义出四个向量
# 将矩阵看成一个有向图，每个单元格对应图中的一个节点，如果相邻的两个单元格
# 的值不相等，则在相邻的两个单元格之间存在一条从较小值指向较大值的有向边。
# 方法一：使用dfs，并且使用缓存矩阵memo存储每一个单元格的最长递增路径
#        这样，在相邻的单元格进行计算时，可以利用先前计算好的单元格中的值
#   那么问题来了，如何保证每一个memo[i][j]记录最长递增路径呢？这个和遍历
#   经过（经过 - 表示从小到大，否则不算经过）它的次数有关。联想到拓扑排序中
#   出度的概念，但这里跟出度不一样。出度最高为4，而最长递增路径跟矩阵数字分布有关
#   dfs最先返回的一定是出度非0的单元格，同时，这个单元格周围所有单元格数值都比它大
#   根据递归栈的特点，调用了dfs的上一个单元格一定是memo[new_i][new_j]+1=2
#   而matrix[i][j]也会倒着走递增的路，将指向它的单元格memo赋值为3，直至递归到有向图的入口点之一
#   遍历矩阵从其他未被访问过的入口点进入时，原先入口点经过的路径上memo值已经确定且不再修改
#   因为即使再次被访问到，根据高低走势，也只能重走“旧路”
# 方法二：上面是从最低谷开始返回，这里利用拓扑排序，从局部最高峰（即入度为0）开始进入

# @lc code=start
import collections
from typing import List


class Solution:
    rows = 0
    columns = 0
    DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # 拓扑排序利用层次遍历，更好理解些
        if matrix is None:
            return 0
        self.rows = len(matrix)
        self.columns = len(matrix[0])
        queue = collections.deque()

        out_degrees = [[0] * self.columns for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.columns):
                for dx, dy in Solution.DIRS:
                    new_row, new_column = i + dx, j + dy
                    if 0 <= new_row < self.rows and 0 <= new_column < \
                            self.columns and matrix[new_row][new_column] > \
                            matrix[i][j]:
                        out_degrees[i][j] += 1
                if out_degrees[i][j] == 0:
                    queue.append((i, j))

        ans = 0
        while queue:
            # 将上一轮收集的单元格同一批处理，按照DIRS搜索一层
            n = len(queue)
            ans += 1
            for _ in range(n):
                row, column = queue.popleft()
                for dx, dy in Solution.DIRS:
                    new_row, new_column = row + dx, column + dy
                    if 0 <= new_row < self.rows and 0 <= new_column < \
                            self.columns and matrix[new_row][new_column] < \
                            matrix[row][column]:
                        out_degrees[new_row][new_column] -= 1
                        if out_degrees[new_row][new_column] == 0:
                            queue.append((new_row, new_column))
        return ans

# @lc code=end
# 1.LeetCode中关于这种矩阵“图”的比较少，这道算是一个很好的例子，并且
# 它将dfs（方法一）和拓扑排序（bfs）/动态规划（方法二）联系到了一起
# 2.coding practice - lru_cache装饰器
# 能够将特定输入的函数结果进行缓存，下次使用同样输入调用函数时，直接返回结果
# 适合递归函数
# 如果不指定传参则默认值为128，表示最多缓存128个返回结果，当达到了128个时，
# 有新的结果要保存时，则会删除最旧的那个结果。如果maxsize传入为None则表示可以缓存无限个结果；
