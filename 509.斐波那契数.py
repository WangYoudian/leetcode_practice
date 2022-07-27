#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start
from functools import lru_cache

class Solution:
    @lru_cache(None)
    def fib(self, n: int) -> int:
        if n in [0, 1]:
            return 0 if n == 0 else 1
        return self.fib(n-1) + self.fib(n-2)
# @lc code=end

