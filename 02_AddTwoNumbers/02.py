# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
            :type l1: ListNode
            :type l2: ListNode
            :rtype: ListNode
            """
        flag = 0
        if l1 == None: return l2
        if l2 == None: return l1
        dummy = ListNode(0); res = dummy
        while l1 and l2:
            res.next = ListNode((l1.val+l2.val+flag) % 10)
            flag = (l1.val+l2.val+flag) / 10
            l1 = l1.next
            l2 = l2.next
            res = res.next
        
        if l2:
            while l2:
                res.next = ListNode((l2.val+flag) % 10)
                flag = (l2.val+flag) / 10
                l2 = l2.next
                res = res.next
        if l1:
            while l1:
                res.next = ListNode((l1.val+flag) % 10)
                flag = (l1.val+flag) / 10
                l1 = l1.next
                res = res.next
    
        if flag == 1: res.next = ListNode(1)
    return dummy.next
