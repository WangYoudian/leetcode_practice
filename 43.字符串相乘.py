#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
# 模拟竖式相乘
# 另外，还可以用卷积的算法

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # 模拟乘法逐个进行运算，最终去掉 ans 数组前导 0
        # 注意 ans[i + j + 1] 是 nums1 的 i 位与 nums2 的 j 位 相乘对应的个位
        res = [0] * (len(num1) + len(num2))
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                tmp = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                tmp += res[i + j + 1]
                # 十位进位
                res[i + j] += tmp // 10
                # 进位后个位对 10 取模
                res[i + j + 1] = tmp % 10
        ans = ''.join(map(str, res))
        # not ans.lstrip('0') 排除 0 的情形
        return '0' if not ans.lstrip('0') else ans.lstrip('0')

# @lc code=end
