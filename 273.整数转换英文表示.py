#
# @lc app=leetcode.cn id=273 lang=python3
#
# [273] 整数转换英文表示
# 
# 1.小于 20 的数可以直接得到其英文表示；
# 2.大于等于 20 且小于 100 的数首先将十位转换成英文表示，然后对个位递归地转换成英文表示；
# 3.大于等于 100 的数首先将百位转换成英文表示，然后对其余部分（十位和个位）递归地转换成英文表示。
# 注意：只有非零的组的英文表示才会拼接到整数 num 的英文表示中；
#      且如果 num=0，则不适用上述做法，而是直接返回 “Zero"。


# @lc code=start
class Solution:
    def numberToWords(self, num: int) -> str:
# @lc code=end

