
class Solution(object):
    """
    @ Google

    One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record
    the node's value. If it is a null node, we record using a sentinel value such as #.

         _9_
        /   \
       3     2
      / \   / \
     4   1  #  6
    / \ / \   / \
    # # # #   # #
    For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents
    a null node.

    Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a
    binary tree. Find an algorithm without reconstructing the tree.

    Each comma separated value in the string must be either an integer or a character '#' representing null pointer.

    You may assume that the input format is always valid, for example it could never contain two consecutive commas
    such as "1,,3".

    Example 1:
    "9,3,4,#,#,1,#,#,2,#,6,#,#"
    Return true

    Example 2:
    "1,#"
    Return false

    Example 3:
    "9,#,#,1"
    Return false
    """
    def isValidSerialization_1(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        stack = []
        for x in preorder.split(','):
            stack.append(x)
            while len(stack) >= 3 and stack[-2:] == ['#', '#'] and stack[-3] != '#':
                stack = stack[:-3] + ['#']
        return len(stack) == 1 and stack[0] == '#'

    def isValidSerialization_2(self, preorder):
        """
        Observation: the outdegrees and indegrees of all nodes in a valid binary tree should be equal.
        :param preorder:
        :return:
        """
        nodes = preorder.split(',')
        diff = 1 # diff = outdegree - indegree
        for node in nodes:
            # first, adding a new node implies the indgrees incremented by 1
            diff -= 1
            if diff < 0: return False
            # second, if the node newly added is non-leaf node, outdgrees incremented by 2
            if node != '#':
                diff += 2
        return diff == 0