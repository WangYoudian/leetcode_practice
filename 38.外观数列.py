#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        def convert(num_str):
            result = ''
            i = 0
            cnt = 0
            while i <= len(num_str) - 1:
                if cnt == 0:
                    cnt += 1
                    i += 1
                    continue
                if num_str[i] == num_str[i-1]:
                    cnt += 1
                    i += 1
                else:
                    result += str(cnt) + num_str[i-1]
                    cnt = 1
                    i += 1
            result += str(cnt) + num_str[i-1]
            return result
        
        ans = '1'
        for k in range(1, n):
            ans = convert(ans)
        return ans

# @lc code=end

