#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:

        if head is None: return None
        
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        print(p)
        l = 0
        while p.next:
            l += 1
            p = p.next
        k = k % l
        if k == 0: return head
        print(p)
        p.next = head
        p = dummy
        step = l - k
        while step > 0:
            p = p.next
            step -= 1
        res = p.next
        p.next = None
        return res