#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
# 方法一：模拟扫描（横向）
# 方法二：列式扫描，利用 zip(*)

# @lc code=start
class Solution:
    # def longestCommonPrefix(self, strs: List[str]) -> str:
    #     if not strs or len(strs) == 0:
    #         return ""
    #     for i in range(len(strs[0])):
    #         c = strs[0][i]
    #         for j in range(1, len(strs)):
    #             # 遇到最短的 word ，或者在第 i 个字符时，没有全部匹配
    #             if i == len(strs[j]) or strs[j][i] != c:
    #                 return strs[0][:i]
    #     # strs[0] 全部匹配
    #     return strs[0]

    def longestCommonPrefix(self, strs: List[str]) -> str:
        # star: ※※  列式扫描 zip(*字符串数组)
        ls = list(zip(*strs))
        prefix = ""
        for item in ls:
            if len(set(item)) == 1:
                prefix += item[0]
            else:
                break
        return prefix

# @lc code=end

