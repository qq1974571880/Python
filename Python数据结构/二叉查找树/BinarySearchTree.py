class Node:

    # 初始化
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:

    # 初始化
    def __init__(self):
        self.root = None

    # 搜索
    def search(self, node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        if node.value > value:
            return self.search(node.left, value)
        else:
            return self.search(node.right, value)

    # 插入
    def insert(self, root: Node, node: Node, value):
        if root == None:
            self.root = Node(value)
        else:
            if node == None:
                if root.value < value:
                    root.right = Node(value)
                else:
                    root.left = Node(value)
            else:
                if node.value < value:
                    self.insert(node, node.right, value)
                else:
                    self.insert(node, node.left, value)


    # 删除
    def delete(self, root, node, value):
        if node == None:
            print("未找到，删除失败")
        elif value == self.root.value:
            print("找到该数，为根节点，已删除数")
            self.root = None
        elif node.value == value:
            if node.left is None and node.right is None:
                print("找到该数，为叶子结点，已删除")
                if root.left == node:
                    root.left = None
                else:
                    root.right = None
            elif node.left is None:
                print("找到该数，只有右子树，已删除")
                if root.left == node:
                    root.left = node.right
                else:
                    root.right = node.right
            elif node.right is None:
                print("找到该数，只有左子树，已删除")
                if root.left == node:
                    root.left = node.left
                else:
                    root.right = node.left
            else:
                print("找到该数，左子树和右子树均不空，已删除")
                minNode = node
                minParentNode = node
                while minNode.left is not None:
                    minParentNode = minNode
                    minNode = minNode.left
                node.value = minNode.value
                minParentNode.left = None
        else:
            if node.value > value:
                self.delete(node, node.left, value)
            else:
                self.delete(node, node.right, value)


    # 先序遍历
    def preOrderTraverse(self, node: Node):
        if node is not None:
            print(node.value)
            self.preOrderTraverse(node.left)
            self.preOrderTraverse(node.right)

    # 中序遍历
    def inOrderTraverse(self, node:Node):
        if node is not None:
            self.inOrderTraverse(node.left)
            print(node.value)
            self.inOrderTraverse(node.right)

    # 后序遍历
    def postOrderTraverse(self, node):
        if node is not None:
            self.postOrderTraverse(node.left)
            self.postOrderTraverse(node.right)
            print(node.value)

if __name__ == "__main__":
    tree = Tree()
    nodeList = [49, 38, 65, 97, 60, 76, 13, 27, 5, 1]
    # nodeList = [5]
    for num in nodeList:
        tree.insert(tree.root, tree.root, num)
    tree.delete(tree.root, tree.root, 97)
    tree.delete(tree.root, tree.root, 76)
    tree.delete(tree.root, tree.root, 13)
    tree.preOrderTraverse(tree.root)
    # tree.inOrderTraverse(tree.root)
    # tree.postOrderTraverse(tree.root)