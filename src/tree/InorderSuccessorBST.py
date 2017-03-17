import unittest


class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree(object):
    @classmethod
    def build_bst(cls, arr, low, high):
        if arr is None or len(arr) == 0:
            return None

        if len(arr) == 1:
            return TreeNode(arr[0])

        mid = (low+high)/2
        root = TreeNode(arr[mid])
        root.left = cls.build_bst(arr, low, mid-1)
        root.right = cls.build_bst(arr, mid+1, high)

        return root


class InorderSuccessorBST(object):
    @classmethod
    def get_inorderSuccessor(cls, root, node):

        if node.right:
            return cls.get_minValue(node.right)

        successor = None
        while root:
            if node.value < root.value:
                successor = root
                root = root.left
            elif node.value > root.value:
                root = root.right
            else:
                break
        return successor

    @classmethod
    def get_minValue(cls, node):

        while node.left:
            node = node.left

        return node


class TestRun(unittest.TestCase):

    def test_OnRightSubtree(self):
        root = TreeNode(20)
        root.right = TreeNode(22)
        root.left = TreeNode(8)
        node = root.left
        target = node
        node.left = TreeNode(4)
        node.right = TreeNode(12)
        node = node.right
        node.left = TreeNode(10)
        expected = node.left
        node.right = TreeNode(14)

        actual = InorderSuccessorBST.get_inorderSuccessor(root, target)
        unittest.TestCase.assertEqual(self, expected, actual)

    def test_OnParent(self):
        root = TreeNode(20)
        root.right = TreeNode(22)
        expected = root
        root.left = TreeNode(8)
        node = root.left
        target = node
        node.left = TreeNode(4)

        actual = InorderSuccessorBST.get_inorderSuccessor(root, target)
        unittest.TestCase.assertEqual(self, expected, actual)

    def test_Root(self):
        root = TreeNode(20)
        target = root
        root.right = TreeNode(22)
        expected = root.right
        root.left = TreeNode(8)
        node = root.left
        node.left = TreeNode(4)
        node.right = TreeNode(12)
        node = node.right
        node.left = TreeNode(10)
        node.right = TreeNode(14)

        actual = InorderSuccessorBST.get_inorderSuccessor(root, target)
        unittest.TestCase.assertEqual(self, expected, actual)


if __name__ == "__main__":
    unittest.main()

