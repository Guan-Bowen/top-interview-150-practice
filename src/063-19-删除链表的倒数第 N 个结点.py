'''
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
'''
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        count = 0
        indexDict = dict()
        ptr = head
        while ptr != None:
            count += 1
            indexDict[count] = ptr
            ptr = ptr.next
        if count == 1: return None
        tar = count - n + 1
        if tar == 1: return indexDict[2]
        (indexDict[tar - 1]).next = (indexDict[tar]).next
        return indexDict[1]