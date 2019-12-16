import Queue
from PythonTools.ReadCSVTool.readCSVTool import csvToList
import unittest


def createNullQueue() -> Queue.MyQueue:
    newQueue = Queue.MyQueue()
    return newQueue


def createQueue() -> Queue.MyQueue:
    newQueue = Queue.MyQueue()
    newQueue.push(1)
    newQueue.push(2)
    return newQueue


class QueueCSVTest(unittest.TestCase):

    def queuePushTest(self):
        csvData = csvToList("Queue/queuePushTest.csv")
        pushNums = csvData["pushNum"]
        expectedResults = csvData["expectedResults"]
        comments = csvData["comments"]
        remarks = csvData["remarks"]
        for index in range(0, len(expectedResults)):
            myStack = createNullQueue()
            myStack.push(pushNums[index])
            expectedResultList = [expectedResults[index]]
            self.assertEqual(expectedResultList, myStack.printQueue(), comments[index])
            print(remarks[index])

    def isEmptyTest(self):
        csvData = csvToList("Queue/isEmptyTest.csv")
        isTrue = csvData["isTrue"]
        comments = csvData["comments"]
        remarks = csvData["remarks"]
        expectedResults = csvData["expectedResults"]
        for index, expectedResult in enumerate(expectedResults):
            queue = createNullQueue() if isTrue[index] else createQueue()
            self.assertEqual(queue.isEmpty(), expectedResult, comments[index])
            print(remarks[index])

    def popTest(self):
        csvData = csvToList("Queue/popTest.csv")
        isNull = csvData["isNull"]
        comments = csvData["comments"]
        remarks = csvData["remarks"]
        expectedResults = csvData["expectedResults"]
        for index, expectedResult in enumerate(expectedResults):
            queue = createNullQueue() if isNull[index] else createQueue()
            queue.pop()

            # list中有数字的话，调用join方法会报错，需要先for循环将其变成str
            queueString = "" if queue.printQueue() is None else ','.join(str(s) for s in queue.printQueue() if s not
                                                                         in ['None', 'NULL'])
            self.assertEqual(queueString, expectedResult, comments[index])
            print(remarks[index])

    def getTopTest(self):
        csvData = csvToList("Queue/getTopTest.csv")
        isNull = csvData["isNull"]
        comments = csvData["comments"]
        remarks = csvData["remarks"]
        expectedResults = csvData["expectedResults"]
        for index, expectedResult in enumerate(expectedResults):
            queue = createNullQueue() if isNull[index] else createQueue()
            queueString = "" if queue.printQueue() is None else ','.join(str(s) for s in queue.printQueue() if s not
                                                                         in ['None', 'NULL'])
            self.assertEqual(expectedResult, queueString, comments[index])
            print(remarks[index])


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(QueueCSVTest('queuePushTest'))
    suite.addTest(QueueCSVTest('isEmptyTest'))
    suite.addTest(QueueCSVTest('popTest'))
    suite.addTest(QueueCSVTest('getTopTest'))
    unittest.TextTestRunner().run(suite)
