# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = l1
        num2 = l2

        new = ListNode()
        res = new
        value = 0
        while num1 or num2 or value == 1:
            
            if num1:
                value += num1.val
                num1 = num1.next
            if num2:
                value += num2.val
                num2 = num2.next
            if value >= 10:
                new.next = ListNode(value % 10)
                value = int(value / 10)
            else:
                new.next = ListNode(value)
                value = 0
            new = new.next
        return res.next