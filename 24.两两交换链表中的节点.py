#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
# 难点：head 是指向数组中第一个元素的，因此本题算是没有头结点的链表
#   那么在交换第 1 和第 2 个节点时，需要用 self 作为头结点， next 指针指向head
#   所幸，在 ListNode 定义中已经满足了

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # Python 中下式等价于 pre = self; pre.next = head
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = pre.next.next
            # star: ※※※  Python 中链表节点赋值推导式
            # swap a and b
            # 基本逻辑是，从左到右，搞定这三个 <node>.next 指向问题
            # pre.next = b
            # a.next = b.next
            # b.next = a
            # 上面三行等价于：
            # pre.next, b.next, a.next = b, a, b.next
            # 或者等价于（总之，三对值之间的相对顺序不变即可）
            pre.next, a.next, b.next = b, b.next, a
            # 可以认为，Python中会自行推导这里的赋值顺序
            
            # pre 相对的后移两个节点
            pre = a
        # self 为虚拟头结点
        return self.next


# @lc code=end

