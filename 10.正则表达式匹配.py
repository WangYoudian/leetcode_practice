#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

# @lc code=start

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        def matches(i, j):
            if i == 0:
                return False
            if p[j-1] == ".":
                return True
            return s[i-1] == p[j-1]

        f = [[False] * (n+1) for _ in range(m+1)]
        f[0][0] = True
        # i, j 为f下标，实际中字符比对使用i-1, j-1
        for i in range(m+1):
            # i从0开始，应对可能存在的p串开头为 [char]* 匹配0次的情形
            # j为模式串下标，要比目标串领先1位
            for j in range(1, n+1):
                # j>=2，默认输入串不会出现*开头，当然若题目没说，也可以检查一下这种语义错误
                if p[j-1] == "*":
                    # 若p[j-1...j]匹配0个字符
                    f[i][j] |= f[i][j-2]
                    # star ※※※※
                    # 递推匹配，类似KMP算法的next数组计算
                    if matches(i, j-1):
                        f[i][j] |= f[i-1][j]
                else:
                    if matches(i, j):
                        f[i][j] |= f[i-1][j-1]
                    
        return f[m][n]
        
# @lc code=end

# 注意：f[i][j]的状态转移必须使用 |= 运算，否则，对于以下情形，计算错误
# "aaa" "ab*a*c*a"
# 这里，若不是或运算，则在ab*a*已经将s串完全匹配，而p串有多余，
# c*匹配0次，最后的a失配