"""
author: Ricardo
email: ricardo_zeng@whu.edu.cn
Define the data structure of rb_tree and rb_tree_node.
Define the algorithms of Red-Black Tree.
"""
BLACK = 1
RED = 0

class RBTreeNode():
    def __init__(self, value = None, color = BLACK):
        self.key = value
        self.parent = None
        self.left = None
        self.right = None
        self.color = color

class RBTree():
    nil = RBTreeNode(value = None, color = BLACK)

    def __init__(self, root = nil, values = None):
        self.root = root
        if values is not None:
            self.RBInsertNodes(values)

    def RBTreeMinimum(self):
        """
        Find minimum node of the RB Tree.
        """
        x = self.root
        while x.left != self.nil:
            x = x.left
        return x

    def RBInsertNodes(self, nodes = []):
        if isinstance(nodes, list):
            for each in nodes:
                self.RBInsert(RBTreeNode(each, color = RED))
        else:
            print("Not invalid argument. Must be list.")

    def LeftRotate(self, x):
        """
        Left Rotate the tree base on node x
        @param x: the given node which need to be left rotated.
        @param type: RBTreeNode

        @return type: None
        """
        y = x.right
        x.right = y.left
        if y.left is not self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is self.nil:
            self.root = y
        elif x is x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
    
    def RightRotate(self, x):
        """
        Right Rotate the tree base on node x
        @param x: the given node which need to be right rotated.
        @param type: RBTreeNode

        @return type: None
        """
        y = x.left
        x.left = y.right
        if y.right is not self.nil:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is self.nil:
            self.root = y
        elif x is x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y
    
    def RBInsert(self, z):
        """
        Insert the given node z into Red-Black Tree.
        @param z: The given node which needed to be insert into the RBTree.
        @param type: RBTreeNode

        @return type: None
        """
        y = self.nil
        x = self.root
        while x is not self.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y is self.nil:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = self.nil
        z.right = self.nil
        z.color = RED
        self.RBInsertFixup(z)
    
    def RBInsertFixup(self, z):
        """
        After insert one new node into the RBTree, the property of the RETree may be changed.
        We need to call the RBInserFixup function to fixup the new RBTree.
        @param z: The given node which has been inserted into the RBTree.
        @param type: RBTreeNode

        @return type: None
        """
        while z.parent.color is RED:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color is RED:
                    z.parent.color = BLACK
                    y.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent
                elif z is z.parent.right:
                    z = z.parent
                    self.LeftRotate(z)
                z.parent.color = BLACK
                z.parent.parent.color = RED
                self.RightRotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color is RED:
                    z.parent.color = BLACK
                    y.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent
                elif z is z.parent.left:
                    z = z.parent
                    self.RightRotate(z)
                z.parent.color = BLACK
                z.parent.parent.color = RED
                self.LeftRotate(z.parent.parent)
        self.root.color = BLACK

    def RBTransPlant(self, u, v):
        """
        Replace a subtree base on node u with a subtree base on node v.
        @param u: the subtree need to be replaced.
        @param type: RBTreeNode

        @param v: the subtree need to replace.
        @param type: RBTreeNode

        @return type: None
        """
        if u.parent is self.nil:
            self.root = v
        elif u is u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent
    
    def RBDelete(self, z):
        """
        Delete node z from Red-Black tree.
        @param z: the node need to be deleted.
        @param type: RBTreeNode

        @return type: None
        """
        y = z
        y_original_color = y.color
        if z.left is self.nil:
            x = z.right
            self.RBTransPlant(z, z.right)
        elif z.right is self.nil:
            x = z.left
            self.RBTransPlant(z, z.left)
        else:
            y = RBTree(root = z.right).RBTreeMinimum()
            y_original_color = y.color
            x = y.right
            if y.parent is z:
                x.parent = y
            else:
                self.RBTransPlant(y, y.right)
                y.right = z.right
                y.right.p = y
            self.RBTransPlant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == BLACK:
            self.RBDeleteFixup(x)
    
    def RBDeleteFixup(self, x):
        while x is not self.root and x.color == BLACK:
            if x is x.parent.left:
                w = x.parent.right
                if w.color == RED:
                    w.color = BLACK
                    x.parent.color = RED
                    self.LeftRotate(x.parent)
                    w = x.parent.right
                if w.left.color == BLACK and w.right.color == BLACK:
                    w.color == RED
                    x = x.parent
                else:
                    if w.right.color == BLACK:
                        w.left.color = BLACK
                        w.color = RED
                        self.RightRotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = BLACK
                    w.right.color = BLACK
                    self.LeftRotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == RED:
                    w.color = BLACK
                    x.parent.color = RED
                    self.RightRotate(x.parent)
                    w = x.parent.right
                if w.left.color == BLACK and w.right.color == BLACK:
                    w.color = RED
                    x = x.parent
                else:
                    if w.left.color == BLACK:
                        w.right.color = BLACK
                        w.color = RED
                        self.LeftRotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = BLACK
                    w.left.color = BLACK
                    self.RightRotate(x.parent)
                    x = self.root
        x.color = BLACK

    def RBInorderTreeWalk(self):
        if self.root is not self.nil:
            if self.root.left is not self.nil:
                RBTree(root = self.root.left).RBInorderTreeWalk()
            print(self.root.key)
            if self.root.right is not self.nil:
                RBTree(root = self.root.right).RBInorderTreeWalk()

    def RBTreeSearch(self, value):
        """
        Find the node of Red-Black tree whose key is value.
        The recursive version of BST tree search.
        @param value: The number which we need to find in the RB-Tree.
        @param type: Number or None
        """
        if self.root is self.nil:
            print("There is no node with such value in this tree.")
            return
        if value == self.root.key:
            return self.root
        elif value < self.root.key:
            return RBTree(self.root.left).RBTreeSearch(value)
        else:
            return RBTree(self.root.right).RBTreeSearch(value)

    def IterativeRBTreeSearch(self, value):
        """
        Find the node of Red-Black tree whose key is value.
        The iterative version of Red-Black tree search.
        @param value: The number which we need to find in the RB-Tree.
        @param type: Number or None
        """
        x = self.root
        if x is self.nil:
            print("There is no node with such value in this tree.")
            return
        while x is not self.nil:
            if value == x.key:
                return x
            elif value < x.key:
                x = x.left
            else:
                x = x.right
        print("There is no node with such value in this tree.")
        return