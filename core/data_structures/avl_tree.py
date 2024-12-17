class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None
    
    def height(self, node):
        """Get height of a node"""
        if not node:
            return 0
        return node.height
    
    def balance_factor(self, node):
        """Calculate balance factor of a node"""
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)
    
    def right_rotate(self, y):
        """Right rotation"""
        x = y.left
        T2 = x.right
        
        # Perform rotation
        x.right = y
        y.left = T2
        
        # Update heights
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        
        return x
    
    def left_rotate(self, x):
        """Left rotation"""
        y = x.right
        T2 = y.left
        
        # Perform rotation
        y.left = x
        x.right = T2
        
        # Update heights
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        
        return y
    
    def insert(self, root, key):
        """Insert a key into AVL tree"""
        # Standard BST insertion
        if not root:
            return AVLNode(key)
        
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        
        # Update height of current node
        root.height = 1 + max(self.height(root.left), self.height(root.right))
        
        # Get balance factor
        balance = self.balance_factor(root)
        
        # Balance the tree
        # Left Left Case
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)
        
        # Right Right Case
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)
        
        # Left Right Case
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        
        # Right Left Case
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        
        return root
    
    def insert_key(self, key):
        """Public method to insert key"""
        self.root = self.insert(self.root, key)
    
    def inorder_traversal(self, root):
        """Inorder traversal of the tree"""
        result = []
        if root:
            result.extend(self.inorder_traversal(root.left))
            result.append(root.key)
            result.extend(self.inorder_traversal(root.right))
        return result
    
    def get_sorted_keys(self):
        """Get sorted keys"""
        return self.inorder_traversal(self.root)