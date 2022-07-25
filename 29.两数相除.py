#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
# 分析：由于 Python 整数位数无限，负数的除法是向下取整的，以及没有 truncate 函数
#   首先需要解决符号问题，其次是使用减法模拟除法运算

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        # star: ※※※ 模拟除法
        ans = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            # 被除数 = 被除数 % (除数*10) + 下一位
            # 通过这种模拟除法的操作还可以对较大数据进行运算

            # ans 每经过一层下面的循环，增加 1...1(若干个1)
            # 关于 1...1 的拓展：https://www.cnblogs.com/xfm666/p/13440551.html
            while dividend >= temp:
                # 由于不能用 mod 运算符，所以只能减去 1 个 除数*10
                dividend -= temp
                ans += i
                i = i << 1
                temp = temp << 1
        if not positive:
            ans = -ans
        return min(max(-2**31, ans), 2**31 - 1)


# @lc code=end

