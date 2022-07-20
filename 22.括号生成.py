#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
from functools import lru_cache
from typing import List


class Solution:
    # 缓存方法调用的结果，加速递归程序栈返回速度
    @lru_cache(None)
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return ['']
        ans = []
        for c in range(n):
            # 当c为0时，left=''
            for left in self.generateParenthesis(c):
                # c为0时，递归处理n-1问题；c>0，问题规模进一步减小
                for right in self.generateParenthesis(n-1-c):
                    ans.append('({}){}'.format(left, right))
        return ans
# @lc code=end

