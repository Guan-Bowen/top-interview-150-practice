'''
给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。
'''
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        count = 0
        indexDict = dict()
        ptr = head
        while ptr != None:
            count += 1
            indexDict[count] = ptr
            ptr = ptr.next
        if count == 0: return head
        k = k % count
        if k == 0: return head
        tar = count - k + 1
        (indexDict[tar - 1]).next = None
        (indexDict[count]).next = head
        return indexDict[tar]