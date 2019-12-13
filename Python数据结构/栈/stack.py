# 实现栈，先进后出
class MyStack:

    # 初始化
    def __init__(self):

        # 设置data为私有属性
        self.__data = []

    # 进栈
    def push(self, x):
        self.__data.append(x)

    # 出栈
    def pop(self):
        if self.__data:
            result = self.__data[-1]
            del self.__data[-1]

    # 获取栈顶元素
    def getTop(self):
        if self.__data:
            return self.__data[-1]
        else:
            return None

    # 判断栈是否为空
    def isEmpty(self) -> bool:
        if self.__data:
            return False
        else:
            return True

    def printStack(self):
        return self.__data


# if __name__ == "__main__":
#     stack = MyStack()
#     print(stack.isEmpty())
#     stack.push(1)
#     stack.push(2)
#     print(stack.getTop())
#     stack.pop()
#     print(stack.isEmpty())
#     print(stack.getTop())
