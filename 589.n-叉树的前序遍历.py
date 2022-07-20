#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N 叉树的前序遍历
#
from collections import deque

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        # 迭代法前序遍历
        q = deque()
        q.append(root)
        ans = []
        while q:
            cur = q.pop()
            ans.append(cur.val)
            if cur.children:
                # children的兄弟之间，越靠右的越在最后遍历，压栈
                for child in cur.children[::-1]:
                    if child:
                        q.append(child)

        return ans
     
# @lc code=end

