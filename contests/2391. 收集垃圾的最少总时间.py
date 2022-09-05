from typing import List


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        n = len(garbage)
        gpm = []

        def amount(mass):
            res = [0] * n
            for k in range(n - 1, -1, -1):
                if k == n - 1:
                    res[k] = garbage[k].count(mass)
                    continue
                res[k] = res[k + 1] + garbage[k].count(mass)
            return res

        gpm.append(amount('G'))
        gpm.append(amount('P'))
        gpm.append(amount('M'))

        ans = 0
        for i in range(3):
            # gpm[i] 中出现 0 ，该行停止计数
            if gpm[i][0] == 0:
                continue
            else:
                ans += gpm[i][0]
            for j in range(1, n):
                if gpm[i][j] == 0 and j > 0:
                    ans += sum(travel[:j - 1])
                    break
                if j == n - 1 and gpm[i][j] != 0:
                    ans += sum(travel)
        return ans


if __name__ == '__main__':
    # garbage = ["G", "P", "GP", "GG"]
    # travel = [2, 4, 3]
    # 21
    garbage = ["MMM", "PGM", "GP"]
    travel = [3, 10]
    # 37
    print(Solution().garbageCollection(garbage, travel))
