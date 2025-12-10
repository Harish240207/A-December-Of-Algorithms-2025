# Reorder Linked List in Zig-Zag Pattern
# Input:
#   Line 1: integer N (number of nodes)
#   Line 2: N space-separated integers (node values)
#
# Output:
#   Reordered linked list values in one line, space-separated

import sys

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def build_linked_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for v in values[1:]:
        current.next = Node(v)
        current = current.next
    return head


def find_middle_and_split(head):
    """
    Uses slow/fast pointers to find the middle.
    Splits the list into two halves and returns (first_head, second_head).
    second_head starts at the middle (or just after) depending on length.
    """
    if not head or not head.next:
        return head, None

    slow = head
    fast = head
    prev = None

    # When fast reaches end, slow is at middle
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    # Split the list into two halves
    prev.next = None  # end first half
    second_head = slow
    return head, second_head


def reverse_list(head):
    prev = None
    current = head
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev


def reorder_list(head):
    if not head or not head.next:
        return head

    # 1. Split into two halves
    first, second = find_middle_and_split(head)

    # 2. Reverse the second half
    second = reverse_list(second)

    # 3. Merge in zig-zag: first node from first list, then from second, etc.
    head1 = first
    head2 = second

    while head2:
        # Save next pointers
        temp1 = head1.next
        temp2 = head2.next

        # Link head1 -> head2
        head1.next = head2
        # Link head2 -> temp1
        head2.next = temp1

        # Move forward
        head1 = temp1 if temp1 else head2  # safe move
        head2 = temp2

    return first


def print_list(head):
    values = []
    current = head
    while current:
        values.append(str(current.val))
        current = current.next
    print(" ".join(values))


def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return

    N = int(data[0])
    values = list(map(int, data[1:1+N]))

    head = build_linked_list(values)
    head = reorder_list(head)
    print_list(head)


if __name__ == "__main__":
    main()