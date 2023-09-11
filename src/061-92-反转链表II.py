'''
给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        pos = 1
        ptr = head
        preOne = None
        while ptr != None:
            tmp = ptr.next
            if pos < left or pos > right: 
                preOne = ptr
            elif pos == left:
                savePoint = ptr
                savePointPre = preOne
                preOne = ptr
            elif pos > left and pos < right:
                ptr.next = preOne
                preOne = ptr
            elif pos == right:
                savePoint.next = ptr.next
                if savePointPre: savePointPre.next = ptr
                savePoint = ptr
                ptr.next = preOne
                preOne = ptr
            ptr = tmp
            pos += 1
        if left == 1: return savePoint
        else: return head