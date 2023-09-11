'''
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = l1.val + l2.val
        if res >= 10: res -= 10; tmp = 1
        else: tmp = 0
        head = ListNode(val=res)
        ptr = head
        l1, l2 = l1.next, l2.next
        while True:
            if not l1 and not l2: break
            res = 0
            if l1: res += l1.val; l1 = l1.next
            if l2: res += l2.val; l2 = l2.next
            res += tmp
            if res >= 10: tmp = 1; res -= 10
            else: tmp = 0
            nextNode = ListNode(val=res)
            ptr.next = nextNode
            ptr = nextNode
        if tmp: 
            finalNode = ListNode(val=tmp)
            ptr.next = finalNode
        return head