'''
给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        indexDict = dict()
        ptr = head
        if not ptr: return None
        cache = []
        while ptr:
            k = ptr.val
            cache.append(k)
            ptr = ptr.next
        cache.sort()
        ptr = head = ListNode(val=cache[0])
        for i in range(1, len(cache)):
            node = ListNode(val=cache[i])
            ptr.next = node
            ptr = node
        return head