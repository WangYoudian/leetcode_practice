#
# @lc app=leetcode.cn id=695 lang=python3
#
# [695] 岛屿的最大面积
#

# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(x, y):
            grid[x][y] = 0
            area = 1
            for d in DIR:
                new_x, new_y = x + d[0], y + d[1]
                if 0<= new_x < m and 0<= new_y<n and \
                    grid[new_x][new_y] == 1:
                    # star ※※※
                    # 注意这里dfs的返回值技巧——
                    # dfs的网格是需要记载并且返回的，通过返回函数内部变量而非函数传参
                    area += dfs(new_x, new_y)
            return area
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans = max(ans, dfs(i, j))
        return ans
        

# @lc code=end

