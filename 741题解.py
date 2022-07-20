from linecache import cache
from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        # 问题的关键是dfs时怎么处理冲突，即到达同一个点 注意到步数是相同的，利用这一点达成
        n = len(grid)

        @cache
        def dfs(x1, x2, k):
            y1 = k - x1
            y2 = k - x2
            if (x1 >= n or y1 >= n or x2 >= n or y2 >= n
                    or grid[x1][y1] == -1 or grid[x2][y2] == -1):
                return float('-inf')

            if x1 == n - 1 and y1 == n - 1:
                return grid[-1][-1]

            ret = grid[x1][y1]
            if x1 != x2:  # 避免重复计数 当前两个坐标的樱桃
                ret += grid[x2][y2]

            return max(dfs(x1, x2, k + 1), dfs(x1 + 1, x2, k + 1),
                       dfs(x1, x2 + 1, k + 1), dfs(x1 + 1, x2 + 1, k + 1)) + ret

        ret = dfs(0, 0, 0)
        return 0 if ret == float('-inf') else ret


if __name__ == "main":
    solution = Solution()
    grid = [[0, 1, -1],
            [1, 0, -1],
            [1, 1, 1]]
    print(solution.cherryPickup(grid))
