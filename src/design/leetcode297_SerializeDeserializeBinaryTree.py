
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec(object):
    """
    @ Linkedin, Google, Uber, Facebook, Amazon, Microsoft, Yahoo, Bloomberg

    Tree, Design
    
    Serialization is the process of converting a data structure or object into a sequence of bits so that it
    can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed
    later in the same or another computer environment.

    Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your
    serialization/deserialization algorithm should work. You just need to ensure that a binary tree can
    be serialized to a string and this string can be deserialized to the original tree structure.

    For example, you may serialize the following tree

        1
       / \
      2   3
         / \
        4   5
    as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a binary tree. You do not necessarily
    need to follow this format, so please be creative and come up with different approaches yourself.
    Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms
    should be stateless.
    """
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        if root is None:
            return str(res)
        curr_level = [root]
        while len(curr_level) > 0:
            next_level = []
            for node in curr_level:
                if node:
                    res.append(node.val)
                    next_level.append(node.left)
                    next_level.append(node.right)
                else:
                    res.append(None)
            if next_level.count(None) == len(next_level):
                break
            curr_level = next_level
        i = len(res)-1
        while i >= 0 and res[i] is None:
            i -= 1
        res = res[:i+1]
        return str(res).replace('None', 'null')
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 2:
            return None
        strs = [v.strip() for v in data[1:len(data)-1].split(',')]
        values = []
        for value in strs:
            if value == 'null':
                values.append(None)
            else:
                values.append(int(value))
        l = 1
        parents = []
        curr_vals = values[:l]
        values = values[l:]
        root = None
        while len(curr_vals) > 0:
            curr_level = []
            if len(parents) == 0:
                root = TreeNode(curr_vals.pop(0))
                curr_level.append(root)
            else:
                for node in parents:
                    value = curr_vals.pop(0) if len(curr_vals) > 0 else None
                    if value is not None:
                        node.left = TreeNode(value)
                        curr_level.append(node.left)
                    value = curr_vals.pop(0) if len(curr_vals) > 0 else None
                    if value is not None:
                        node.right = TreeNode(value)
                        curr_level.append(node.right)
            parents = curr_level
            l = 2 * len(parents)
            curr_vals = values[:l]
            values = values[l:]
        return root
        
        
if __name__ == "__main__":
    root = TreeNode(1)
    node2 = TreeNode(3)
    node3 = TreeNode(4)
    node4 = TreeNode(4)
    node5 = TreeNode(5)

    root.left = node2
    node2.right = node3


    codec = Codec()
    data = codec.serialize(root)
    res = codec.deserialize(data)
    print res