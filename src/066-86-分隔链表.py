'''
给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。

你应当 保留 两个分区中每个节点的初始相对位置。
'''
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        ltxList = []
        gtxList = []
        ptr = head
        while ptr != None:
            if ptr.val < x: ltxList.append(ptr)
            else: gtxList.append(ptr)
            ptr = ptr.next
        len1, len2 = len(ltxList), len(gtxList)
        if len1 + len2 <= 1: return head
        if len1 != 0: ptr1 = head1 = ltxList[0]
        else: ptr1 = head1 = None
        if len2 != 0: ptr2 = head2 = gtxList[0]
        else: ptr2 = head2 = None
        for i in range(1, len1):
            ptr1.next = ltxList[i]
            ptr1 = ptr1.next
        if head1: ptr1.next = None
        for i in range(1, len2):
            ptr2.next = gtxList[i]
            ptr2 = ptr2.next
        if head2: ptr2.next = None
        if not head1: return head2
        else:
            ptr1.next = head2
            return head1