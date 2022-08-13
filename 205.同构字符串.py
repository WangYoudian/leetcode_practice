#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#

# @lc code=start
from collections import defaultdict


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = defaultdict()
        # 保证不同字符不能映射到同一个字符上
        visited = set()

        for i, char in enumerate(s):
            if char in mapping:
                if t[i] != mapping[char]:
                    return False
            else:
                if t[i] in visited:
                    return False
                else:
                    visited.add(t[i])
                    mapping[char] = t[i]
        # 字符之间映射表为一对一关系
        return len(set(s)) == len(set(t))

# @lc code=end

