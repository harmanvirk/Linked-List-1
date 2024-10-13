# Time Complexity = O(n) | Space Complexity = O(1)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        flag = False
        if head is None: return None
        slow = head
        fast = head
        while fast is not None and fast.next is not None:  # handle even odd case
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                flag = True
                break

        if not flag: return None

        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow

