import Queue


def createNullQueue() -> Queue.MyQueue:
    newQueue = Queue.MyQueue()
    return newQueue


def createQueue() -> Queue.MyQueue:
    newQueue = Queue.MyQueue()
    newQueue.push(1)
    return newQueue


def queuePushTest():
    myStack = createNullQueue()
    exceptedResult = [1]
    myStack.push(1)
    result = True
    if myStack.printQueue() != exceptedResult:
        result = False
    if result:
        print("queuePushTest测试通过")
    else:
        print("queuePushTest测试失败")


def isEmptyTest():
    testCase = [createNullQueue(), createQueue()]
    exceptedResults = [True, False]
    result = True
    for index, exceptedResult in enumerate(exceptedResults):
        if testCase[index].isEmpty() != exceptedResult:
            result = False
            break
    if result:
        print("isEmptyTest测试通过")
    else:
        print("isEmptyTest测试失败")


def popTest():
    testCase = [createQueue()]
    exceptedResults = [[]]
    result = True
    for index, exceptedResult in enumerate(exceptedResults):
        testCase[index].pop()
        if testCase[index].printQueue() != exceptedResult:
            result = False
            break
    if result:
        print("pop测试通过")
    else:
        print("pop测试失败")


def getTopTest():
    testCase = [createNullQueue(), createQueue()]
    exceptedResults = [None, 1]
    result = True
    for index, exceptedResult in enumerate(exceptedResults):
        if testCase[index].getTop() != exceptedResult:
            result = False
            break
    if result:
        print("getTopTest测试通过")
    else:
        print("getTopTest测试失败")


if __name__ == "__main__":
    queuePushTest()
    isEmptyTest()
    popTest()
    getTopTest()
