#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#
import copy



# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        result = []
        for digit in digits:
            temp = []
            if len(result) == 0:
                result = mapping[digit]
                continue                    
            for ch in mapping[digit]:
                for comb in result:
                    comb += ch
                    temp.append(comb)
            result = temp
        return result


# @lc code=end

