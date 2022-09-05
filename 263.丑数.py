#
# @lc app=leetcode.cn id=263 lang=python3
#
# [263] 丑数
#

# @lc code=start
class Solution:
    def isUgly(self, n: int) -> bool:
        factors = [2, 3, 5]
        for i, factor in enumerate(factors):
            while n > 1:
                if i == len(factors) - 1 and n % factor != 0:
                    return False
                # 不是最后一个因子，则就继续分解下一个因子
                elif n % factor != 0:
                    break
                n //= factor
        return n == 1
                
# @lc code=end

