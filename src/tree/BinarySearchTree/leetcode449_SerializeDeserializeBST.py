
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    """
    @ Amazon

    Tree


    Serialization is the process of converting a data structure or object into
    a sequence of bits so that it can be stored in a file or memory buffer, or
    transmitted across a network connection link to be reconstructed later in
    the same or another computer environment.

    Design an algorithm to serialize and deserialize a binary search tree. There is
    no restriction on how your serialization/deserialization algorithm should work.
    You just need to ensure that a binary search tree can be serialized to a string
    and this string can be deserialized to the original tree structure.

    The encoded string should be as compact as possible.

    Note: Do not use class member/global/static variables to store states. Your
    serialize and deserialize algorithms should be stateless.
    """

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def preorder(root):
            if root:
                vals.append(str(root.val))
                preorder(root.left)
                preorder(root.right)

        vals = []
        preorder(root)
        return ' '.join(vals)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def buildBST(preorder, inorder):
            if len(inorder) == 0:
                return None
            val = preorder.pop(0)
            root = TreeNode(val)
            x = inorder.index(val)
            root.left = buildBST(preorder, inorder[:x])
            root.right = buildBST(preorder, inorder[ x +1:])
            return root

        preorder = map(int, data.split())
        inorder = sorted(preorder)
        return buildBST(preorder, inorder)


if __name__ == "__main__":
    node1 = TreeNode(2)
    node2 = TreeNode(1)
    node3 = TreeNode(3)

    root = node1
    root.left = node2
    root.right = node3

    data = Codec().serialize(root)
    Codec().deserialize(data)
    print data
