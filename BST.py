__author__ = 'tianzhang'

# Implement basic operation of binary search tree
# Assume that all values are distinct

import Queue


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
# Iterative Insertion
def insert(root, x):
    if root is None:
        return TreeNode(x)
    else:
        node = root
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
    return root
'''


# Recursive Insertion
def insert(root, x):
    if root is None:
        return TreeNode(x)
    else:
        if root.val < x:
            root.right = insert(root.right, x)
        else:
            root.left = insert(root.left, x)
    return root


'''
# Iterative Search
def search(root, x):
    node = root
    while node is not None:
        if node.val == x:
            return True
        elif node.val < x:
            node = node.right
        else:
            node = node.left
    return False
'''


# Recursive Search
def search(root, x):
    if root is None:
        return False
    else:
        if root.val == x:
            return True
        elif root.val < x:
            return search(root.right, x)
        else:
            return search(root.left, x)


'''
# Iterative finding max/min
def find_max(root):
    if root is None:
        return None
    node = root
    tracker = None
    while node is not None:
        tracker = node
        node = node.right
    return tracker.val
'''


# Recursive finding max/min
def find_max(root):
    if root is None:
        return None
    else:
        if root.right is None:
            return root.val
        else:
            return find_max(root.right)


def find_min(root):
    if root is None:
        return None
    else:
        if root.left is None:
            return root.val
        else:
            return find_min(root.left)


# Iterative deletion is sooooooooo complicated! Just use recursive deletion...
def delete(root, x):
    if root is None:
        return None
    else:
        if root.val < x:
            root.right = delete(root.right, x)
        elif root.val > x:
            root.left = delete(root.left, x)
        else:  # Real deletion
            # Case1: no child
            if root.left is None and root.right is None:
                root = None
            # Case2: one child
            elif root.left is None:
                root = root.right
            elif root.right is None:
                root = root.left
            # Case3: two children - replace root's value with min in right subtree, delete this min
            else:
                root.val = find_min(root.right)
                root.right = delete(root.right, root.val)
        return root


def find_successor(root, x):
    if root is None:
        return None
    ancestor = None
    node = root
    while node is not None:
        if node.val < x:
            node = node.right
        elif node.val > x:
            ancestor = node
            node = node.left
        else:  # Find successor
            # Step1: find min in right subtree
            if node.right is not None:
                return find_min(node.right)
            # Step2: find first 'right' ancestor
            if ancestor is not None:
                return ancestor.val
            # Step3: already max
            break
    return None


def BFS_output(root):
    if root is None:
        return []
    q = Queue.Queue()
    q.put(root)
    result = []
    while not q.empty():
        node = q.get()
        result.append(node.val)
        if node.left is not None:
            q.put(node.left)
        if node.right is not None:
            q.put(node.right)
    return result


def DFS_output(root, list):
    if root is not None:
        if root.left is not None:
            DFS_output(root.left, list)
        list.append(root.val)
        if root.right is not None:
            DFS_output(root.right, list)
    return list


if __name__ == '__main__':
    nodes = [7, 5, 10, 2, 8, 13, 9, 11, 6, 12]
    root = None
    for node in nodes:
        print 'insert ' + str(node)
        root = insert(root, node)
        print DFS_output(root, [])
    print search(root, 4)
    print search(root, 8)
    print find_max(root)
    print DFS_output(delete(root, 10), [])
    print find_successor(root, 5)
    print find_successor(root, 13)
    print BFS_output(root)
