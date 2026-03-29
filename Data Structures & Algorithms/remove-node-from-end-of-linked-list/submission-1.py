# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        two pointers, one slow one fast. the fast one moves up to n, and then the slow one moves
        so once the fast one is at the end, the slow one is at the pointer to remove
        """
        dummy = ListNode(0, head)
        slow = dummy
        fast = head
        for i in range(0, n):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        # remove next element
        slow.next = slow.next.next

        return dummy.next