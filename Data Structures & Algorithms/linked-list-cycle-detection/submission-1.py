# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

      sp = head
      fp = head

      while fp.next and fp.next.next:

        sp = sp.next
        fp = fp.next.next

        if sp.next == fp.next.next:
          return True

      return False
        