
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Edge case: empty list
        if not lists:
            return None

        # Recursive divide and conquer
        def merge(lists, left, right):
            if left == right:
                return lists[left]
            mid = (left + right) // 2
            l1 = merge(lists, left, mid)
            l2 = merge(lists, mid + 1, right)
            return self.mergeTwoLists(l1, l2)

        return merge(lists, 0, len(lists) - 1)

    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        # Append remaining nodes
        current.next = l1 if l1 else l2
        return dummy.next
