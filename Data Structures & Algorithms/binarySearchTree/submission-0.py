class TreeNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        newNode = TreeNode(key, val)
        if self.root == None:
            self.root = newNode
            return
        current = self.root
        while True:
            if key < current.key:
                if current.left == None:
                    current.left = newNode
                    return
                current = current.left
            elif key > current.key:
                if current.right == None:
                    current.right = newNode
                    return
                current = current.right
            else:
                current.val = val
                return
    
    def get(self, key: int) -> int:
        current = self.root
        while current:
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                return current.val
        return -1

    def getMin(self) -> int:
        current = self.root
        if not current:
            return -1
        while current != None and current.left != None:
            current = current.left
        return current.val

    def getMax(self) -> int:
        current = self.root
        if not current:
            return -1
        while current != None and current.right != None:
            current = current.right
        return current.val

    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)

    def findMin(self, node: TreeNode) -> TreeNode:
        while node and node.left:
            node = node.left
        return node

    def removeHelper(self, current: TreeNode, key: int) -> TreeNode:
        if not current:
            return None

        if key > current.key:
            current.right = removeHelper(current.right, key)
        elif key < current.key:
            current.left = removeHelper(current.left, key)
        else:
            if current.left == None:
                return current.right
            elif current.right == None:
                return current.left
            else:
                minNode = self.findMin(current.right)
                current.key = minNode.key
                current.val = minNode.val
                current.right = self.removeHelper(current.right, minNode.key)
        return current

    def getInorderKeys(self) -> List[int]:
        result = []
        self.inorderTraversal(self.root, result)
        return result
        
    def inorderTraversal(self, root: TreeNode, result: List[int]) -> None:
        if root != None:
            self.inorderTraversal(root.left, result)
            result.append(root.key)
            self.inorderTraversal(root.right, result)
