import LinkedList
import os
import sys

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
    results = True
    for index, exceptedResult in enumerate(exceptedResults):
        header = testList[index]
        if exceptedResult != header.isEmpty():
            results = False
            print(str(index + 1) + "error")
            break
    return results


if __name__ == "__main__":
    if isEmptyTest():
        print("isEmpty测试通过")
    else:
        print("isEmpty测试失败")
