# coding: utf-8
import DBTool


def createSQL() -> list:
    result = []
    for i1 in range(10):
        for i2 in range(10):
            for i3 in range(10):
                for i4 in range(10):
                    result.append(
                        str(i1) + "\\" + str(i2) + "\\" + str(i3) + "\\" + str(i4) + "\\")
    return result


if __name__ == '__main__':
    DBTool.insertParams(["path", "num"], "folders", createSQL())

