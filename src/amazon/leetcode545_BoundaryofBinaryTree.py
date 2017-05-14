
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
    @ Amazon, Google
    
    Tree
    
    Given a binary tree, return the values of its boundary in anti-clockwise direction starting from root. 
    Boundary includes left boundary, leaves, and right boundary in order without duplicate nodes.

    Left boundary is defined as the path from root to the left-most node. Right boundary is defined as the 
    path from root to the right-most node. If the root doesn't have left subtree or right subtree, then the 
    root itself is left boundary or right boundary. Note this definition only applies to the input binary 
    tree, and not applies to any subtrees.
    
    The left-most node is defined as a leaf node you could reach when you always firstly travel to the left 
    subtree if exists. If not, travel to the right subtree. Repeat until you reach a leaf node.
    
    The right-most node is also defined by the same way with left and right exchanged.
    
    Example 1
    Input:
      1
       \
        2
       / \
      3   4
    
    Ouput:
    [1, 3, 4, 2]
    
    Explanation:
    The root doesn't have left subtree, so the root itself is left boundary.
    The leaves are node 3 and 4.
    The right boundary are node 1,2,4. Note the anti-clockwise direction means you should output reversed 
    right boundary.
    So order them in anti-clockwise without duplicates and we have [1,3,4,2].
    Example 2
    Input:
        ____1_____
       /          \
      2            3
     / \          / 
    4   5        6   
       / \      / \
      7   8    9  10  
           
    Ouput:
    [1,2,4,7,8,9,10,6,3]
    
    Explanation:
    The left boundary are node 1,2,4. (4 is the left-most node according to definition)
    The leaves are node 4,7,8,9,10.
    The right boundary are node 1,3,6,10. (10 is the right-most node).
    So order them in anti-clockwise without duplicate nodes we have [1,2,4,7,8,9,10,6,3].
    """
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        if not root.left and not root.right:
            return [root.val]

        lb = [root]
        if root.left:
            self.get_leftBoundary(root.left, lb)
            self.get_leaves(root.left, lb)

        rb = []
        if root.right:
            self.get_rightBoundary(root.right, rb)
            self.get_leaves(root.right, lb)

        for node in rb[::-1]:
            if node not in lb:
                lb.append(node)

        res = [node.val for node in lb]
        return res

    def get_leftBoundary(self, node, lb):
        lb.append(node)
        if node.left:
            self.get_leftBoundary(node.left, lb)
        elif node.right:
            self.get_leftBoundary(node.right, lb)

    def get_rightBoundary(self, node, rb):
        rb.append(node)
        if node.right:
            self.get_rightBoundary(node.right, rb)
        elif node.left:
            self.get_rightBoundary(node.left, rb)

    def get_leaves(self, node, leaves):
        if not node.left and not node.right:
            if node not in leaves:
                leaves.append(node)
            return
        if node.left:
            self.get_leaves(node.left, leaves)
        if node.right:
            self.get_leaves(node.right, leaves)

