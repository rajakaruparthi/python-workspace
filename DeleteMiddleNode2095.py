class DeleteMiddleNode2095:
    def deleteMiddleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
            dummyNode = ListNode(next=head)
            slow_pointer, fast_pointer = dummyNode, head

            # 1->2->3->4->5

            while fast_pointer and fast_pointer.next:
                slow_pointer = slow_pointer.next
                fast_pointer = fast_pointer.next.next

            slow_pointer.next = slow_pointer.next.next

            return dummyNode.next


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
