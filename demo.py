# test_example.py
import unittest

def add(a, b):
    """简单的加法函数"""
    return a + b

def divide(a, b):
    """除法函数，如果除数为0则抛出异常"""
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b

class TestMathOperations(unittest.TestCase):
    """测试数学运算"""
    
    # 通过的测试用例
    def test_add_positive_numbers(self):
        """测试正数加法"""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(10, 20), 30)
    
    def test_add_negative_numbers(self):
        """测试负数加法"""
        self.assertEqual(add(-2, -3), -5)
        self.assertEqual(add(-10, 5), -5)
    
    def test_divide_normal_case(self):
        """测试正常除法"""
        self.assertAlmostEqual(divide(10, 2), 5.0)
        self.assertAlmostEqual(divide(7, 3), 2.3333333333333335)
    
    # 未通过的测试用例
    def test_add_wrong_result(self):
        """这个测试会失败：错误的预期结果"""
        self.assertEqual(add(2, 2), 5)  # 错误：2+2应该等于4，不是5
    
    def test_divide_by_zero(self):
        """这个测试会失败：没有正确处理除零异常"""
        # 这里应该会抛出异常，但测试期望正常返回
        result = divide(10, 0)  # 这里会抛出ValueError
        self.assertEqual(result, 0)  # 这行不会执行
    
    def test_divide_wrong_type(self):
        """这个测试会失败：类型错误"""
        # 尝试用字符串做除法
        result = divide("10", 2)  # 这里会抛出TypeError
        self.assertEqual(result, 5)

class TestStringOperations(unittest.TestCase):
    """测试字符串操作"""
    
    # 通过的测试用例
    def test_string_concatenation(self):
        """测试字符串拼接"""
        result = "Hello" + " " + "World"
        self.assertEqual(result, "Hello World")
        self.assertIn("World", result)
    
    def test_string_methods(self):
        """测试字符串方法"""
        text = "Python UnitTest"
        self.assertTrue(text.startswith("Python"))
        self.assertFalse(text.endswith("Java"))
    
    # 未通过的测试用例
    def test_string_comparison(self):
        """这个测试会失败：字符串比较错误"""
        self.assertEqual("hello".upper(), "HELLO ")  # 错误：多了空格
    
    def test_nonexistent_method(self):
        """这个测试会失败：调用不存在的方法"""
        text = "test"
        result = text.nonexistent_method()  # 这里会抛出AttributeError
        self.assertEqual(result, "expected")

if __name__ == '__main__':
    # 运行测试
    unittest.main(verbosity=2)
