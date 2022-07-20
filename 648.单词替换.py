#
# @lc app=leetcode.cn id=648 lang=python3
#
# [648] 单词替换
#
# 方法一：哈希
# 方法二：字典树
# 将dictionary中的成员构建成字典树的同时，需要在每个单词末尾插上
# 一个特殊字符'#'，标识这是一个前缀的结束。在搜索前缀时，只需要在
# 字典树上搜索出一条最短的前缀路径即可——即当前节点的孩子节点有结束标志'#'

# @lc code=start

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = {}
        for word in dictionary:
            cur = trie
            for c in word:
                # 注意，必须先判断not in，否则无法建出正确的字典树
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
                # 错误写法，例如当trie为空，单词cat输入时，树的第二层会出现c/a/t/#
                # c/a/t不是子孙关系而成了兄弟关系，显然违背了字典树的初衷
                # 对于初始单词而言，由于没有“前路”供借鉴，前后字符之间一定是父子关系
                # 建trie过程有点类似链表的插入过程
                # 而从第二个单词之后，对于可能出现的公共前缀，必然要利用，同时保证单词内
                # 前后字符之间的父子关系 - cur = cur[c]
                # if c in cur:
                #     cur = cur[c]
                # else:
                #     cur[c] = {}
            cur['#'] = {}


        ans = []
        words = sentence.split(' ')
        for word in words:
            # 字典树的搜索节点
            cur = trie
            n = len(word)
            for j, ch in enumerate(word):
                # word还有字符未经查找，就提前遇到结束标识，即trie中的最短前缀
                # 当前单词的[1...j-1]字母直接输出
                if '#' in cur:
                    ans.append(word[:j])
                    break
                # 未找到任何前缀，则直接输出单词，并退出这个单词的字符遍历
                # 注意：未找到任何前缀包括：1.word[j]不在trie的非结束标志的孩子中
                #       以及2.word的字符所在的**最短前缀树长度**长于len(word)，
                # 例如：['a', 'bsm', 'aa'] 'a bs aa'，若不判断j与word长度关系，则只会输出a
                if ch not in cur or n == j + 1:
                    ans.append(word)
                    break
                
                # 又成功匹配一次，前缀自然加长 -- j += 1，继续在字典树往下遍历
                cur = cur[ch]
        return ' '.join(ans)

# @lc code=end
# 评价：官方给的参考答案里，用的in-place的方式，让word长度短于最短前缀长时，
#       for word in words循环正常退出，但道理其实和上面n = j + 1判断是一样的
#       不过in-place做法可以节省O(sentence)的空间
