import stack


def createNullStack() -> stack.MyStack:
    newStack = stack.MyStack()
    return newStack


def createStack() -> stack.MyStack:
    newStack = stack.MyStack()
    newStack.push(1)
    return newStack


def stackPushTest():
    myStack = createNullStack()
    exceptedResult = [1]
    myStack.push(1)
    result = True
    if myStack.printStack() != exceptedResult:
        result = False
    if result:
        print("stackPushTest测试通过")
    else:
        print("stackPushTest测试失败")


def isEmptyTest():
    testCase = [createNullStack(), createStack()]
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
    testCase = [createStack()]
    exceptedResults = [[]]
    result = True
    for index, exceptedResult in enumerate(exceptedResults):
        testCase[index].pop()
        if testCase[index].printStack() != exceptedResult:
            result = False
            break
    if result:
        print("pop测试通过")
    else:
        print("pop测试失败")


def getTopTest():
    testCase = [createNullStack(), createStack()]
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
    stackPushTest()
    isEmptyTest()
    popTest()
    getTopTest()
