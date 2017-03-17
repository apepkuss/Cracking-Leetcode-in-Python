
class TreeNode(object):
    def __init__(self, value):
        self.parent = None
        self.left = None
        self.right = None
        self.value = value
        self.color = "RED"


class RBTree(object):
    root = None

########################### INSERTION ##############################
    @classmethod
    def insert_value(cls, value):  # O(logn) time
        node = TreeNode(value)
        cls.insert_node(node)

    @classmethod
    def insert_node(cls, node):
        if cls.root is None:
            cls.insert_case1(node)
        else:
            parent = cls.root
            while parent:
                if parent.value > node.value:
                    if parent.left:
                        parent = parent.left
                    else:
                        parent.left = node
                        node.parent = parent
                        cls.insert_case1(node)
                        break
                else:
                    if parent.right:
                        parent = parent.right
                    else:
                        parent.right = node
                        node.parent = parent
                        cls.insert_case1(node)
                        break

    @classmethod
    def insert_case1(cls, node):
        # case1: root is None
        if cls.root is None:
            cls.root = node
            cls.root.color = "BLACK"
        else:
            cls.insert_case2(node)

    @classmethod
    def insert_case2(cls, node):
        # case2: parent's color is black
        if node.parent.color == "BLACK":
            return
        else:
            cls.insert_case3(node)

    @classmethod
    def insert_case3(cls, node):
        # case3: parent's and its sibling's color are red
        uncle = cls.get_uncle(node)
        if uncle is not None and uncle.color == "RED":
            node.parent.color = "BLACK"
            uncle.color = "BLACK"
            grandparent = cls.get_grandparent(node)
            grandparent.color = "RED"
            cls.insert_case1(grandparent)
        else:
            cls.insert_case4(node)

    @classmethod
    def insert_case4(cls, node):
        # case4: parent's color is red, but its sibling's color is black;
        grandparent = cls.get_grandparent(node)
        # LR
        if (node == node.parent.right) and (node.parent == grandparent.left):
            # rotate left: LR -> LL
            cls.rotate_left(node.parent)
            node = node.left
        # RL
        elif (node == node.parent.left) and (node.parent == grandparent.right):
            # rotate right: RL -> RR
            cls.rotate_right(node.parent)
            node = node.right

        # deal with LL and RR
        cls.insert_case5(node)

    @classmethod
    def insert_case5(cls, node):
        # case5: LL or RR
        grandparent = cls.get_grandparent(node)
        node.parent.color = "BLACK"
        grandparent.color = "RED"
        # LL
        if node == node.parent.left:
            # rotate right
            cls.rotate_right(grandparent)
        # RR
        else:
            # rotate left
            cls.rotate_left(grandparent)


########################### SEARCH ##############################

    @classmethod
    def search_node(cls, value):  # O(logn) time
        node = cls.root
        while node:
            if node.value == value:
                return node
            else:
                node = node.left if value < node.value else node.right
        return None


########################### DELETION ##############################

    @classmethod
    def delete_value(cls, value):  # O(logn) time
        node = cls.search_node(value)
        if node:
            cls.delete_node(node)
        else:
            print "No such a value: " + value

    @classmethod
    def delete_node(cls, node):
        if cls.is_leaf(node.left) or cls.is_leaf(node.right):
            cls.delete_one_child(node)
        else:
            child = node.right
            while child.left:
                child = child.left
            parent = child.parent
            parent.parent.left = parent.right
            parent.right.parent = parent.parent
            node.value = parent.value
            del parent

    @classmethod
    def delete_one_child(cls, node):
        # precondition: node has at most one non-leaf child
        child = node.left if cls.is_leaf(node.right) else node.right

        cls.replace_node(node, child)
        if node.color == "BLACK":
            if child.color == "RED":
                child.color = "BLACK"
            else:
                cls.delete_case1(child)
        del node

    @classmethod
    def delete_case1(cls, node):
        if node.parent is None:
            return
        else:
            cls.delete_case2(node)

    @classmethod
    def delete_case2(cls, node):
        sibling = cls.get_sibling(node)

        if sibling.color == "RED":
            node.parent.color = "RED"
            sibling.color = "BLACK"
            if node == node.parent.left:
                cls.rotate_left(node.parent)
            else:
                cls.rotate_right(node.parent)

        cls.delete_case3(node)

    @classmethod
    def delete_case3(cls, node):
        sibling = RBTree.get_sibling(node)

        if node.parent.color == "BLACK" and sibling.color == "BLACK" and sibling.left == "BLACK" and sibling.right == "BLACK":
            sibling.color = "RED"
            cls.delete_case1(node.parent)
        else:
            cls.delete_case4(node)

    @classmethod
    def delete_case4(cls, node):
        sibling = RBTree.get_sibling(node)

        if node.parent.color == "RED" and sibling.color == "BLACK" and sibling.left == "BLACK" and sibling.right == "BLACK":
            sibling.color = "RED"
            node.parent.color = "BLACK"
        else:
            cls.delete_case5(node)

    @classmethod
    def delete_case5(cls, node):
        sibling = cls.get_sibling(node)

        if sibling.color == "BLACK":
            if node == node.parent.left and sibling.left == "RED" and sibling.right == "BLACK":
                sibling.color = "RED"
                sibling.left.color = "BLACK"
                cls.rotate_right(sibling)
            elif node == node.parent.left and sibling.left == "BLACK" and sibling.right == "RED":
                sibling.color = "RED"
                sibling.right.color = "BLACK"
                cls.rotate_left(sibling)

        cls.delete_case6(node)

    @classmethod
    def delete_case6(cls, node):
        sibling = cls.get_sibling(node)

        sibling.color = node.parent.color
        node.parent.color = "BLACK"

        if node == node.parent.left:
            sibling.right.color = "BLACK"
            cls.rotate_left(node.parent)
        else:
            sibling.left.color = "BLACK"
            cls.rotate_right(node.parent)


######################### HELPER METHODS ############################
    @classmethod
    def get_grandparent(cls, node):
        if node is not None and node.parent is not None:
            return node.parent.parent
        else:
            return None

    @classmethod
    def get_uncle(cls, node):
        grandparent = cls.get_grandparent(node)
        if grandparent is None:
            return None
        if node.parent == grandparent.left:
            return grandparent.right
        else:
            return grandparent.left

    @classmethod
    def is_leaf(cls, node):
        if node.left or node.right:
            return False
        return True

    @classmethod
    def replace_node(cls, node, child):
        # precondition: node has at most one non-leaf child
        child.parent = node.parent

        if child == node.left:
            child.right = node.right
        else:
            child.left = node.left

    @classmethod
    def get_sibling(cls, node):
        if node is None or node.parent is None:
            return None
        if node == node.parent.left:
            return node.parent.right
        else:
            return node.parent.left

    @classmethod
    def rotate_left(cls, node):
        child = node.right
        child.parent = node.parent
        node.parent = child
        node.right = child.left
        child.left.parent = node
        child.left = node

    @classmethod
    def rotate_right(cls, node):
        child = node.left
        child.parent = node.parent
        node.parent = child
        node.left = child.right
        child.right.parent = node
        child.right = node





