import LinkedList


def createLinkList() -> LinkedList:
    linkList = LinkedList.LinkedList()
    node1 = LinkedList.Node(1)
    node2 = LinkedList.Node(2)
    node3 = LinkedList.Node(3)
    node4 = LinkedList.Node(4)
    linkList.appendNode(node1)
    linkList.appendNode(node2)
    linkList.appendNode(node3)
    linkList.appendNode(node4)
    return linkList


def createNoneLinkList() -> LinkedList:
    return LinkedList.LinkedList()


def isEmptyTest():
    exceptedResults = [False, True]
    testList = [createLinkList(), createNoneLinkList()]
    result = True
    for index, exceptedResult in enumerate(exceptedResults):
        header = testList[index]
        if exceptedResult != header.isEmpty():
            result = False
            print(str(index + 1) + "error")
            break
    if result:
        print("isEmpty测试通过")
    else:
        print("isEmpty测试失败")


def checkInLinkedListTest():
    testList = createLinkList()
    testCase = [2, 3, 5, 0, -1]
    exceptedResults = [True, True, False, True, False]
    result = True
    for index, exceptedResult in enumerate(exceptedResults):
        if exceptedResult != testList.checkInLinkedList(testCase[index]):
            result = False
            break
    if result:
        print("checkInLinkedListTest测试通过")
    else:
        print("checkInLinkedListTest测试失败")


def appendNodeTest():
    testList = createNoneLinkList()
    exceptedResults = [[1], [1, 2]]
    result = True
    for index, exceptedResult in enumerate(exceptedResults):
        node = LinkedList.Node(index + 1)
        testList.appendNode(node)
        if exceptedResult != testList.printNode():
            result = False
            break
    if result:
        print("appendNodeTest测试通过")
    else:
        print("appendNodeTest测试失败")


def deleteNodeByIndexTest():
    exceptedResults = [[1, 2, 3], [2, 3, 4]]
    testCase = [3, 0]
    result = True
    for index, exceptedResult in enumerate(exceptedResults):
        testList = createLinkList()
        testList.deleteNodeByIndex(testCase[index])
        if exceptedResult != testList.printNode():
            result = False
            break
    if result:
        print("deleteNodeByIndexTest测试通过")
    else:
        print("deleteNodeByIndexTest测试失败")


def deleteNodeByDataTest():
    exceptedResults = [[1, 2, 3], [1, 2, 3, 4]]
    testCase = [4, -1]
    result = True
    for index, exceptedResult in enumerate(exceptedResults):
        testList = createLinkList()
        testList.deleteNodeByData(testCase[index])
        if testList.printNode() != exceptedResult:
            result = False
            break
    if result:
        print("deleteNodeByDataTest测试通过")
    else:
        print("deleteNodeByDataTest测试失败")


def findDataTest():
    exceptedResults = [True, False]
    testCase = [4, 5]
    testList = createLinkList()
    result = True
    for index, exceptedResult in enumerate(exceptedResults):
        if testList.findData(testCase[index]) != exceptedResult:
            result = False
            break
    if result:
        print("findDataTest测试通过")
    else:
        print("findDataTest测试失败")


def updateDataByIndexTest():
    exceptedResults = [[1, 2, 3, 5], [1, 2, 3, 4]]
    testCase = [[3, 5], [-1, 10]]
    result = True
    for index, exceptedResult in enumerate(exceptedResults):
        testList = createLinkList()
        testList.updateDataByIndex(testCase[index][0], testCase[index][1])
        if testList.printNode() != exceptedResult:
            result = False
            break
    if result:
        print("updateDataByIndexTest测试通过")
    else:
        print("updateDataByIndexTest测试失败")


def printNodeTest():
    exceptedResults = [[1, 2, 3, 4], []]
    testList = [createLinkList(), createNoneLinkList()]
    result = True
    for index, exceptedResult in enumerate(exceptedResults):
        tmpList = testList[index]
        if tmpList.printNode() != exceptedResult:
            result = False
            break
    if result:
        print("printNode测试通过")
    else:
        print("printNode测试失败")


def insertNodeByIndexTest():
    exceptedResults = [[0, 1, 2, 3, 4], [1, 2, 3, 4, 5], [1, 1, 2, 3, 4]]
    testCase = [[0, 0], [4, 5], [1, 1]]
    result = True
    for index, exceptedResult in enumerate(exceptedResults):
        node = LinkedList.Node(testCase[index][1])
        tmpList = createLinkList()
        tmpList.insertNodeByIndex(testCase[index][0], node)
        if tmpList.printNode() != exceptedResult:
            print(tmpList.printNode())
            print(exceptedResult)
            result = False
            break
    if result:
        print("insertNodeByIndexTest测试通过")
    else:
        print("insertNodeByIndexTest测试失败")


def getLinkListLengthTest():
    exceptedResults = [4, 0]
    testList = [createLinkList(), createNoneLinkList()]
    result = True
    for index, exceptedResult in enumerate(exceptedResults):
        tmpList = testList[index]
        if tmpList.getLinkListLength() != exceptedResult:
            result = False
            break
    if result:
        print("getLinkListLengthTest测试通过")
    else:
        print("getLinkListLengthTest测试失败")


def clearTest():
    testList = createLinkList()
    if not testList.clear():
        print("clear测试通过")
    else:
        print("clear测试失败")


if __name__ == "__main__":
    isEmptyTest()
    printNodeTest()
    clearTest()
    getLinkListLengthTest()
    checkInLinkedListTest()
    appendNodeTest()
    insertNodeByIndexTest()
    deleteNodeByIndexTest()
    deleteNodeByDataTest()
    updateDataByIndexTest()
    findDataTest()
