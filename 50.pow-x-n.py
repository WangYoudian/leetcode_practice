#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
# 分析：快速幂算法，2^n -> 2^(n // 2)
# 注意：当 n 为负数时，不能对负数进行 n // 2 迭代， Python 的负数除法不同

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quick_pow(k):
            if k == 0:
                return 1.0
            y = quick_pow(k // 2)
            return y * y if k % 2 == 0 else y * y * x
        return quick_pow(n) if n >= 0 else 1.0 / quick_pow(-n)

# @lc code=end
