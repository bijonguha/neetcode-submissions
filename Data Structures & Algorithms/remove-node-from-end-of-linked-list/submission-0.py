# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy
        tail = cur

        i = 0

        while tail.next:
            i+=1
            tail = tail.next

        t = i-n

        j=0
        while j<t:
            j+=1
            cur = cur.next

        if cur.next and cur.next.next:
            cur.next = cur.next.next
        else:
            cur.next = None

        return dummy.next