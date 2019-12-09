# 实现栈，先进后出
class MyStack:

    # 初始化
    def __init__(self):

        # 设置data为私有属性
        self.data = []

    # 进栈
    def push(self, x: int):
        self.data.append(x)

    # 出栈
    def pop(self):
        if self.data:
            del self.data[-1]

    # 获取栈顶元素
    def getTop(self):
        return self.data[-1]

    # 判断栈是否为空
    def isEmpty(self):
        if self.data:
            return False
        else:
            return True


if __name__ == "__main__":
    stack = MyStack()
    print(stack.isEmpty())
    stack.push(1)
    stack.push(2)
    print(stack.getTop())
    stack.pop()
    print(stack.isEmpty())
    print(stack.getTop())
