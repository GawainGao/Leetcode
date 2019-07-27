# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
            :type l1: ListNode
            :type l2: ListNode
            :rtype: ListNode
            """
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        dummy = ListNode(0)
        res = dummy
        
        while l1 and l2:
            if l1.val > l2.val:
                res.next = l2
                res = res.next
                l2 = l2.next
            else:
                res.next = l1
                res = res.next
                l1 = l1.next
if l1:
    res.next = l1
        if l2:
            res.next = l2
    return dummy.next

