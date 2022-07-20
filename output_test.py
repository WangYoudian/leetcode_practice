from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n = len(heights), len(heights[0])

        def flood(edges):
            visited = set()

            def dfs(x, y):
                if (x, y) in visited:
                    return
                visited.add((x, y))
                for dx, dy in DIR:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and \
                            heights[nx][ny] >= heights[x][y]:
                        dfs(nx, ny)

            for ex, ey in edges:
                dfs(ex, ey)
            return visited

        pacific = [(i, 0) for i in range(m)] + [(0, i) for i in range(1, n)]
        atlantic = [(i, n - 1) for i in range(m)] + [(m - 1, i) for i in
                                                     range(n - 1)]
        return list(map(list, flood(pacific) & flood(atlantic)))


if __name__ == '__main__':
    solution = Solution()
    heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1],
               [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
    print(solution.pacificAtlantic(heights))
