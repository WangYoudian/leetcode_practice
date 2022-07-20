#
# @lc app=leetcode.cn id=187 lang=python3
#
# [187] 重复的DNA序列
#
# 常规方法：字符串哈希表
# 进阶方法：滑动窗口+位运算


# @lc code=start
class Solution:
    # def findRepeatedDnaSequences(self, s: str) -> List[str]:
    #     ans = []
    #     d = {}
    #     # 下面的代码可以优化为判断defaultdict的某项刚好等于2时，将substr添加到ans中
    #     # （目的：避免不重不漏）
    #     for i in range(0, len(s)-9):
    #         if s[i:i+10] in d:
    #             d[s[i:i+10]] += 1
    #         else:
    #             d[s[i:i+10]] = 1
    #     for key, value in d.items():
    #         if value > 1:
    #             ans.append(key)
    #     return ans
    
    
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans = []
        n = len(s)
        L = 10
        if n <= L:
            return ans
        gene_dict = {'A': 0, 'T': 1, 'C': 2, 'G': 3}
        # 用x记录滑动窗口内基因字符串重编码后相等的int数值
        x = 0
        # 这里只能选取前L-1位，避免与下一个循环中的移位操作边界冲突
        for i in range(L-1):
            x = (x << 2) | gene_dict[s[i]]
        cnt = defaultdict(int)
        for j in range(n - L + 1):
            # 窗口最左端字符离开，由于只考虑前20个比特，这里使用与运算，表示做差
            # Todo:为什么是1左移20位？
            x = ((x << 2) | gene_dict[s[j+L-1]]) & ((1 << (2*L)) - 1)
            cnt[x] += 1
            if cnt[x] == 2:
                ans.append(s[j:j+L])
        
        return ans
            

# @lc code=end

