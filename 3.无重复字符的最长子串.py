#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
# 模拟扫描

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # start 记录子数组起始位置
        # star: ※※※  利用字典和下标配合，既能取到最大，又不多算无效字符（start前的字符）
        start = 0
        ans = 0
        sub_dict = {}
        for i in range(len(s)):
            if s[i] in sub_dict and start <= sub_dict[s[i]]:
                start = sub_dict[s[i]] + 1
            else:
                # 注意：不要等到出现重复字符才开始记录 ans ，
                #   答案必须是 子串 的长度，而不是子序列
                #   因此，重复字符出现，则更新字典中该字符的位置
                #   且需要判断字符位置与 start 的关系，可以知道是否为前面出现的
                #   若是，则不用更新
                ans = max(ans, i - start + 1)
            sub_dict[s[i]] = i
        return ans

# @lc code=end

