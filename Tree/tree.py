"""
author: Ricardo
email: ricardo_zeng@whu.edu.cn
Define the data structure of tree and tree_node.
Define the algorithms of Binary Search T.
"""
class TreeNode:
    def __init__(self, value = None):
        self.key = value
        self.parent = None
        self.left = None
        self.right = None

    def IsLeaf(self):
        return self.left is None and self.right is None

class Tree:
    def __init__(self, root = None):
        self.root = root        #The type of parameter root is TreeNode
    
    def InorderTreeWalk(self):
        if self.root is not None:
            if self.root.left is not None:
                Tree(root = self.root.left).InorderTreeWalk()
            print(self.root.key)
            if self.root.right is not None:
                Tree(root = self.root.right).InorderTreeWalk()
    
    def TreeSearch(self, value):
        """
        Find the node of BST tree whose key is value.
        @param value: The number which we need to find in the BST.
        @param type: Number
        """
        x = self.root
        if x is None:
            return None
        while x is not None:
            if value is x.key:
                return x
            elif value < x.key:
                x = x.left
            else:
                x = x.right
        return None
    
    def IterativeTreeSearch(self, value):
        """
        The iterative version of BST tree search.
        @param value: The number which we need to find in the BST.
        @param type: Number
        """
        if self.root is None:
            return
        if value is self.root.key:
            return self.root
        elif value < self.root.key:
            return Tree(self.root.left).IterativeTreeSearch(value)
        else:
            return Tree(self.root.right).IterativeTreeSearch(value)
    
    def TreeMinimum(self):
        """
        Find minimum node of the BST T.
        """
        x = self.root
        while x.left != None:
            x = x.left
        return x

    def TreeMaximum(self):
        """
        Find maximum node of the BST T.
        """
        x = self.root
        while x.right != None:
            x = x.right
        return x
    
    def TreeSuccessor(self, x):
        """
        Find the successor of the given tree node x.
        @param x: The given tree node.
        @param type: TreeNode
        """
        if x.right is not None:
            return Tree(root = x.right).TreeMinimum()
        y = x.parent
        while (y is not None) and (x is y.right):
            x = y
            y = y.parent
        return y

    def TreeInsert(self, key):
        """
        Inser the new node into the Binary Search T.
        @param key: The number need to be insert.
        @param type: Number
        """
        if self.root is None:
            self.root = TreeNode(value = key)
        else:
            z = TreeNode(value = key)
            y = None
            x = self.root
            while x is not None:
                y = x
                if key < x.key:
                    x = x.left
                else:
                    x = x.right
            z.parent = y
            if z.key < y.key:
                y.left = z
            else:
                y.right = z
    
    def TransPlant(self):
        pass
    
    def TreeDelete(self):
        pass

if __name__ == "__main__":
    t = Tree()
    t.TreeInsert(9)
    t.TreeInsert(3)
    t.TreeInsert(4)
    t.TreeInsert(5)
    t.TreeInsert(2)
    t.TreeInsert(7)
    t.TreeInsert(1)
    t.InorderTreeWalk()
    print(t.TreeSuccessor(t.TreeSearch(5)))