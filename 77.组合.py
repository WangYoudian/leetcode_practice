#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#
from itertools import combinations

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        for comb in combinations(range(1, n+1), k):
            ans.append(list(comb))
        return ans

# @lc code=end

