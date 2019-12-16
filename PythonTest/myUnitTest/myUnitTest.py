import unittest


class MyTest(unittest.TestCase):  # 继承unittest.TestCase
    def tearDown(self):
        # 每个测试用例执行之后做操作
        print('111')

    def setUp(self):
        # 每个测试用例执行之前做操作
        print('22222')

    @classmethod
    def tearDownClass(self):
        # 必须使用 @ classmethod装饰器, 所有test运行完后运行一次
        print('4444444')

    @classmethod
    def setUpClass(self):
        # 必须使用@classmethod 装饰器,所有test运行前运行一次
        print('33333')

    def test_a_run(self):
        self.assertEqual(1, 1)  # 测试用例
        print("test_a_run")

    def test_b_run(self):
        self.assertEqual(2, 2)  # 测试用例


if __name__ == '__main__':
    unittest.main()  # 运行所有的测试用例
    # 常用测试用例
    # assertEqual(a, b)
    # a == b
    # assertNotEqual(a, b)
    # a != b
    # assertTrue(x)
    # bool(x) is True
    # assertFalse(x)
    # bool(x) is False
    # assertIsNone(x)
    # x is None
    # assertIsNotNone(x)
    # x is not None
    # assertIn(a, b)
    # a in b
    # assertNotIn(a, b)
    # a not in b