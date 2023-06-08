from dataclasses import dataclass


@dataclass
class ListNode:
    val: int = 0
    next: 'ListNode' = None


class Solution:
    """https://leetcode.com/problems/reverse-linked-list/"""

    def reverseList(self, head: ListNode | None) -> ListNode | None:
        result = None
        while head is not None:
            result = ListNode(head.val, result)
            head = head.next
        return result
