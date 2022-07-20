#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
# 分析：只需要排除无限循环的可能，即可在有限次重复将结果收敛到1

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        def square_sum(a):
            res = 0
            while a > 0:
                res += (a % 10)**2
                a //= 10
            return res
        
        # 从初始值到重复过程，记录所有的中间值，若中间某次计算得到
        # 的结果在集合中，则证明存在一个无限循环，程序退出
        unhappy_set = {n}
        while n != 1:
            n = square_sum(n)
            if n in unhappy_set:
                return False
            else:
                unhappy_set.add(n)
        return True

# @lc code=end

