'''
给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        cache = []
        for node in lists:
            ptr = node
            while ptr:
                cache.append(ptr.val)
                ptr = ptr.next
        cache.sort()
        n = len(cache)
        if not n: return None
        ptr = head = ListNode(val=cache[0])
        for i in range(1, n):
            node = ListNode(val=cache[i])
            ptr.next = node
            ptr = node
        return head
        