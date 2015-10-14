__author__ = 'tianzhang'

# Implement basic operation of binary search tree
# Assume that all values are distinct

import Queue
import random

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    # In order
    def DFSFunc(self, list):
        if self.left is not None:
            self.left.DFSFunc(list)
        list.append(self.val)
        if self.right is not None:
            self.right.DFSFunc(list)
        return list

class BST:
    def __init__(self):
        self.root = None

    def insert(self, x):
        if self.root is None:
            self.root = TreeNode(x)
        else:
            node = self.root
            tracker = None
            while node is not None:
                tracker = node
                if node.val < x:
                    node = node.right
                else:
                    node = node.left
            new = TreeNode(x)
            if tracker.val > x:
                tracker.left = new
            else:
                tracker.right = new

    def search(self, x):
        node = self.root
        while node is not None:
            if node.val == x:
                return True
            elif node.val < x:
                node = node.right
            else:
                node = node.left
        return False

    def BFS_output(self):
        if self.root is None:
            return []
        q = Queue.Queue()
        q.put(self.root)
        result = []
        while not q.empty():
            node = q.get()
            result.append(node.val)
            if node.left is not None:
                q.put(node.left)
            if node.right is not None:
                q.put(node.right)
        return result

    def DFS_output(self):
        if self.root is None:
            return []
        return self.root.DFSFunc([])

    def remove(self, x):
        if self.root is None:
            return False
        node = self.root
        fake = TreeNode(-1)
        fake.left = self.root
        tracker = fake
        while node is not None:
            if node.val == x:
                # Remove
                # Case1: one or both child is None
                if node.left is None:
                    if tracker.left == node:
                        tracker.left = node.right
                    else:
                        tracker.right = node.right
                elif node.right is None:
                    if tracker.left == node:
                        tracker.left = node.left
                    else:
                        tracker.right = node.left
                # Case2: two children
                else:
                    # Case2.1: node.left.right or node.right.left is None
                    if node.left.right is None:
                        if tracker.left == node:
                            tracker.left = node.left
                        else:
                            tracker.right = node.left
                        node.left.right = node.right
                    elif node.right.left is None:
                        if tracker.left == node:
                            tracker.left = node.right
                        else:
                            tracker.right = node.right
                        node.right.left = node.left
                    # Case2.2
                    else:
                        if tracker.left == node:
                            tracker.left = node.left
                        else:
                            tracker.right = node.left
                        temp = node.left
                        while temp is not None:
                            tracker = temp
                            temp = temp.right
                        tracker.right = node.right
                self.root = fake.left
                return True
            tracker = node
            if node.val < x:
                node = node.right
            else:
                node = node.left
        return False

    def max(self):
        if self.root is None:
            return None
        node = self.root
        tracker = None
        while node is not None:
            tracker = node
            node = node.right
        return tracker.val

    def find_successor(self, x):
        if self.root is None:
            return None
        ancestor = None
        node = self.root
        while node is not None:
            if node.val == x:
                # Find successor
                # Step1: find minimum in right subtree
                if node.right is not None:
                    temp = node.right
                    tracker = node
                    while temp is not None:
                        tracker = temp
                        temp = temp.left
                    return tracker.val
                # Step2: find first "right" ancestor
                if ancestor is not None:
                    return ancestor.val
                # Step3
                break
            elif node.val < x:
                node = node.right
            else:
                ancestor = node
                node = node.left
        return None


if __name__ == '__main__':
    events = [("in", 7), ("in", 5), ("in", 10), ("rm", 7), ("in", 2), ("in", 8), ("in", 13), ("in", 9), ("in", 11), ("rm", 10), ("in", 15), ("in", 6), ("in", 12), ("in", 7)]
    test = BST()
    for event in events:
        print event
        if event[0] == 'in':
            test.insert(event[1])
        if event[0] == 'rm':
            test.remove(event[1])
        print test.DFS_output()
    print test.search(4)
    print test.search(8)
    print test.BFS_output()
    print test.max()
    print test.find_successor(2)
    print test.find_successor(12)
