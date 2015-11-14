__author__ = 'tianzhang'


class LinkedListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def find_middle(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
    return slow


if __name__ == '__main__':
    values = [1,2,3,4,5,6,7,8]
    print values
    head = LinkedListNode(values[0])
    current = head
    for i in range(1, len(values)):
        new = LinkedListNode(values[i])
        current.next = new
        current = new

    middle = find_middle(head)
    print middle.val

