# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        curr1 = list1
        curr2 = list2

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                # Connect the smaller node to tail
                tail.next = curr1
                curr1 = curr1.next
                # Move curr1 forward
            else:
                # Connect the smaller node to tail
                tail.next = curr2
                # Move curr2 forward
                curr2 = curr2.next

            # Advance tail
            tail = tail.next

    # Attach whichever list still has nodes
        tail.next = curr1 or curr2

        return dummy.next

    # Return the first actual node
            