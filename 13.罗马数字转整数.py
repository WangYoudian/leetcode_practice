#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        d ={
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        n = len(s)
        ans = 0
        jump = False
        for i, ch in enumerate(s):
            if jump:
                jump = False
                continue
            if ch == "I" and i < n-1:
                if s[i+1] in ["V", "X"]:
                    ans += d[s[i:i+2]]
                    jump = True
                    continue
            if ch == "X" and i < n-1:
                if s[i+1] in ["L", "C"]:
                    ans += d[s[i:i+2]]
                    jump = True
                    continue
            if ch == "C" and i < n-1:
                if s[i+1] in ["D", "M"]:
                    ans += d[s[i:i+2]]
                    jump = True
                    continue
            ans += d[ch]
            
        return ans



# @lc code=end

