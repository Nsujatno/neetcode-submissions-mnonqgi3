# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        So basically we gonna traverse the list and we wanna reverse it in order.
        we can do this by taking the curr nodes next pointer and point it behind
        to iterate we need to keep track of the temporary next one
        """
        prev = None
        curr = head
        while curr:
            temp = curr.next
            # set curr next value equal to the one before
            curr.next = prev
            
            # iterate
            prev = curr
            if temp:
                curr = temp
            else:
                return curr