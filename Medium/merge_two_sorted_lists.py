from typing import ListNode, Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 if list1 else list2

        return dummy.next



# Test

if __name__ == "__main__":
    s = Solution()
    # Example usage of mergeTwoLists
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    merged_list = s.mergeTwoLists(list1, list2)
    while merged_list:
        print(merged_list.val, end=" -> ")
        merged_list = merged_list.next
    print("None")
    
    print(s.reverseVowels("hello"))  # Output: "holle"
    print(s.reverseVowels("leetcode"))  # Output: "leotcede"
    print(s.reverseVowels("aA"))  # Output: "Aa"
