#
# @lc app=leetcode.cn id=1281 lang=python3
#
# [1281] 整数的各位积和之差
#

# @lc code=start
from functools import reduce


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        bits = []
        while n > 0:
            rest = n % 10
            n //= 10
            bits.append(rest)
        s = sum(bits)
        t = reduce(lambda x, y: x * y, bits)
        return t - s

# @lc code=end

