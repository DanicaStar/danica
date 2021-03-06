'''
1、导入unittest
2、创建测试类，继承unittest.TestCase
3、特殊方法（非必输）——test fixture
    setup        在每个测试用例执行前执行
    teardown     在每个测试用例执行后执行
    setupclass    在测试类执行前执行——在测试类中所有测试用例执行前先执行，需要@classmethod修饰
    teardownclass 在测试类执行后执行——在测试类中所有测试用例执行后再执行，需要@classmethod修饰
4、测试用例
5、普通方法
'''


# 1、导入unittest
import unittest
# 2、创建测试类，继承unittest.TestCase
class Test_Demo_1(unittest.TestCase):
# 3、特殊方法（非必输）——test fixture
    def setUp(self):
        print("setUp 在每个测试用例执行前执行一次")


    def tearDown(self):
        print("tearDown 在每个测试用例执行后执行一次")

    @classmethod
    def setUpClass(cls): #在测试类中只执行一次
        print("setUpClass 在所有测试用例执行前执行一次")
        print('打开浏览器')
    @classmethod
    def tearDownClass(cls):   #在测试类中只执行一次
        print("tearDownClass 在所有测试用例执行后执行一次")
        print('关闭浏览器')

# 4、测试用例
#     @unittest.skip('需求变更')
    def test_case_01(self):
        '''全部填写注册'''
        print('全部填写注册')
        self.assertEqual('tom','lily',msg="比较条件不相等")

    def test_case_02(self):
        '''只填写必填项注册'''
        print('只填写必填项注册')
        self.assertTrue('a'=='a',msg='')

    def test_case_02(self):
        '''不勾选协议注册'''
        print('不勾选协议注册')
        self.assertTrue('a'=='a',msg='')
# 5、普通方法


if __name__ == '__main__':
    unittest.main()


