'''
给定一个已排序的链表的头 head ， 删除原始链表中所有重复数字的节点，只留下不同的数字 。返回 已排序的链表 。
'''
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ptr = head
        uniList = list()
        valueList = list()
        while ptr != None:
            valueList.append(ptr.val)
            ptr = ptr.next
        for num in valueList:
            if valueList.count(num) == 1: uniList.append(num)
        l = len(uniList)
        if l == 0: return None
        head = ListNode(val=uniList[0])
        if l == 1: return head
        ptr = head
        for i in range(1, l):
            newNode = ListNode(val=uniList[i])
            ptr.next = newNode
            ptr = newNode
        return head