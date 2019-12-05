class Node:

    # 初始化，为data赋值
    def __init__(self, data, nextNode=None):
        self.data = data
        self.next = nextNode

    # 为data赋值
    def setData(self, data):
        self.setData(data)

    # 获取data的值
    def getData(self):
        return self.data

    # 设置Next指向，默认为None
    def setNode(self, node=None):
        self.next = node

    # 获取Next指向
    def getNext(self):
        return self.next


class LinkedList:

    # 初始化
    def __init__(self):
        self.header = None

    # 检测链表是否为空
    def isEmpty(self):
        return self.header is None

    # 检测目录是否位于链表内
    def checkInLinkedList(self, index):
        return True if index < self.getLinkListLength() else False

    # 寻找指定坐标的前一个节点
    def getFrontNodeByIndex(self, index) -> Node:
        if self.checkInLinkedList(index):
            count = 0
            currentTmp = self.header
            frontTmp = self.header
            while count != index:
                count += 1
                frontTmp = currentTmp
                currentTmp = currentTmp.getNext()
            return frontTmp
        else:
            return None

    # 为链表添加元素
    def appendNode(self, node):
        if self.isEmpty():
            self.header = node
        else:
            currentTmp = self.header
            while currentTmp.getNext() is not None:
                currentTmp = currentTmp.getNext()
            currentTmp.setNode(node)

    # 在指定坐标插入指定元素
    def insertNodeByIndex(self, index, node):
        length = self.getLinkListLength()
        if index > length:
            return False
        if index == length:
            self.appendNode(node)
        else:
            frontTmp = self.getFrontNodeByIndex(index)
            currentTmp = frontTmp.getNext()
            node.setNode(currentTmp)
            frontTmp.setNode(node)
        return True

    # 删除指定坐标的元素
    def deleteNodeByIndex(self, index):
        if self.checkInLinkedList(index):
            if index == 0:
                self.header = self.header.getNext()
            else:
                frontTmp = self.getFrontNodeByIndex(index)
                currentTmp = frontTmp.getNext()
                frontTmp.setNode(currentTmp.getNext())
            return True
        else:
            return False

    # 删除指定data的元素
    def deleteNodeByData(self, data):
        currentTmp = self.header
        frontTmp = self.header
        while currentTmp is not None:
            frontTmp = currentTmp
            if data == currentTmp.data:
                frontTmp.setNode(currentTmp.getNext())
                return True
            else:
                currentTmp = currentTmp.getNext()
        return False

    # 依据坐标修正data
    def updateDataByIndex(self, index, data):
        if self.checkInLinkedList(index):
            if index == 0:
                self.header.setData = data
            else:
                fromtTmp = self.getFrontNodeByIndex(index)
                fromtTmp.getNext().setData(data)
            return True
        return False

    # 查询指定data的Node是否存在
    def findData(self, data):
        currentTmp = self.header
        while currentTmp is not None:
            if currentTmp.data == data:
                return True
            else:
                currentTmp = currentTmp.getNext()
        return False

    # 获取链表长度
    def getLinkListLength(self):
        if self.header is None:
            return 0
        else:
            count = 0
            currentTmp = self.header
            while currentTmp is not None:
                count += 1
                currentTmp = currentTmp.getNext()
            return count

    # 输出链表全部元素
    def printNode(self):
        if self.header is not None:
            currentTmp = self.header
            printList  = []
            while currentTmp is not None:
                printList.append(currentTmp.data)
                currentTmp = currentTmp.next
            print(printList)
        else:
            print("链表为空")

    # 清空链表
    def clear(self):
        self.header = None


# if __name__ == "__main__":
#     linkList = LinkedList()
#     node1 = Node(1)
#     node2 = Node(2)
#     node3 = Node(3)
#     node4 = Node(4)
#     linkList.appendNode(node1)
#     linkList.appendNode(node2)
#     linkList.appendNode(node3)
#     linkList.printNode()
#     print(linkList.getLinkListLength())
#     print(linkList.insertNodeByIndex(1, node4))
#     linkList.printNode()
#     print(linkList.deleteNodeByData(4))
#     linkList.printNode()
#     print(linkList.deleteNodeByIndex(10))
#     print(linkList.deleteNodeByIndex(0))
#     print(linkList.deleteNodeByIndex(1))
#     linkList.printNode()
#     print(linkList.findData(3))
#     print(linkList.findData(5))
