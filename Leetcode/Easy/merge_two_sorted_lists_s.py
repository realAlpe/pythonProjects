from dataclasses import dataclass


@dataclass
class ListNode:
    val: int = 0
    next: 'ListNode' = None


class Solution:
    """https://leetcode.com/problems/merge-two-sorted-lists/"""

    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        cur = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2

        if list1 or list2:
            cur.next = list1 if list1 else list2

        return dummy.next


a = ListNode(1, ListNode(2, ListNode(4)))
b = ListNode(1, ListNode(3, ListNode(4)))
print(Solution().mergeTwoLists(a, b))
