'''
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        valueList = []
        while list1 != None:
            valueList.append(list1.val)
            list1 = list1.next
        while list2 != None:
            valueList.append(list2.val)
            list2 = list2.next
        n = len(valueList)
        if n == 0: return None
        valueList.sort()
        head = ListNode(val=valueList[0])
        ptr = head
        for i in range(1, n):
            newNode = ListNode(val=valueList[i])
            ptr.next = newNode
            ptr = newNode
        return head
