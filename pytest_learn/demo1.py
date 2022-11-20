# # 测试函数形式
# def test_func():  # 要求函数名以 test 开头
#     """测试函数"""
#     print('我是测试函数')

# 测试类形式
import pytest


class TestDemo(object):  # 正常定义类, 但是测试类名必须以 Test 开头
    """测试示例类"""

    def test_method1(self):  # 正常定义方法, 但是测试方法名必须以 test 开头
        """测试方法1"""
        print('测试方法1')

    def test_method2(self):
        """测试方法2"""
        print('测试方法2')


if __name__ == '__main__':
    pytest.main(['-s', 'demo1.py'])
