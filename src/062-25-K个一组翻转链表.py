'''
给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。

k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        count = 1
        headFlag = False
        cache = []
        res = []
        ptr = head
        while ptr != None:
            newNode = ListNode(val=ptr.val)
            cache.append(newNode)
            if count == k:
                cache.reverse()
                for i in range(k - 1):
                    (cache[i]).next = cache[i + 1]
                if res: (res[-1]).next = cache[0]
                res = res + cache
                cache = []
                count = 1
            else:
                count += 1
            ptr = ptr.next
        if cache:
            if res: 
                (res[-1]).next = cache[0]
                for i in range(len(cache) - 1): (cache[i]).next = cache[i + 1]
        return res[0]
            