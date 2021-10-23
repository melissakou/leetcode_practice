from utils import timer

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    
    # Solution 1: Set
    @timer
    def detectCycle(self, head):
        if head is None:
            return None
        seen_node = set()
        while head.next is not None:
            if head.next in seen_node is not None:
                return head.next
            seen_node.add(head)
            head = head.next
        return None

    # Solution 2: Slow & Fast Pointers
    @timer
    def detectCycle(self, head):
        if head is None or head.next is None or head.next.next is None:
            return None
        slow = head.next
        fast = head.next.next
        while slow != fast:
            if fast.next is None or fast.next.next is None:
                return None
            slow = slow.next ; fast = fast.next.next
        fast = head
        while slow != fast:
            slow = slow.next ; fast = fast.next
        return slow


if __name__ == "__main__":
    sol = Solution()
    # Example 1
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next
    print(sol.detectCycle(head).val)

    # Example 2
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = head
    print(sol.detectCycle(head).val)

    # Example 3
    head = ListNode(1)
    print(sol.detectCycle(head))