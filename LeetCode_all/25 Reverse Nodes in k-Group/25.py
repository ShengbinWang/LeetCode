# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        ptr = head

        def revLink(head, k):
            new_head, ptr = None, head

            while k:
                nex = ptr.next
                ptr.next = new_head
                new_head = ptr
                ptr = nex
                k -= 1

            return new_head

        while count < k and ptr:
            ptr = ptr.next
            count += 1

        if count == k:
            newHead = revLink(head, k)
            head.next = self.reverseKGroup(ptr, k)
            return newHead
        return head
