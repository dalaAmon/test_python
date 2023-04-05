# @Time :2023-4-1 20:44
# @Author :TK
# @Describe :  unittest  测试类下的所有方法都必须以test开头，不然无法执行；setup,teardown是非必要条件，
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
'''
class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:   #最先执行。每一条测试用例开始前做的操作，实例化浏览器，获取url，设置等待，
        print('setupClass...')
        cls.driver= webdriver.Edge()
        cls.driver.get('http://www.baidu.com')
        cls.driver.maximize_window()

    # def setUp(self) -> None:    #每一次执行测试用例都会执行一次setUp（）和tearDown（）操作，如果有100条测试用例，则会执行100次setUp（），会减低测试效率，故而引入setUpclass（）和teardownclass（）
    #     print('setup...')

    def test01(self):
        print('test01')
        # self.assertEqual(1+2,3)
        self.driver.find_element(By.ID,'kw').send_keys('table')

    def test02(self):
        print('test02')
        self.assertGreaterEqual(5,4)

    # def tearDown(self) -> None:
    #     print('tearDown...')



    @classmethod
    def tearDownClass(cls) -> None:    #最后执行，测试完成后的清除工作，关闭浏览器，数据库的还原
        print('teardownClass...')
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()'''

class MyTestCase01(unittest.TestCase):
    def test01(self):
        print('test01')
        # self.assertEqual(1+2,3)
        # self.driver.find_element(By.ID, 'kw').send_keys('table')

    def test02(self):
        print('test02')
        # self.assertGreaterEqual(5, 4)

class MyTestCase02(unittest.TestCase):
    def test03(self):
        print('test03')
        # self.assertEqual(1+2,3)
        # self.driver.find_element(By.ID, 'kw').send_keys('table')

    def test04(self):
        print('test04')

if __name__ == '__main__':
    loader=unittest.TestLoader()    #加载器
    suite=unittest.TestSuite()     #测试套件
    # suite.addTest(loader.loadTestsFromTestCase(MyTestCase01))
    # suite.addTest(loader.loadTestsFromTestCase(MyTestCase02))

    # suite.addTest(loader.loadTestsFromModule(MyTestCase01))    #通过用例模板加载测试用例
    # suite.addTest(loader.loadTestsFromModule(MyTestCase02))

    path=os.path.dirname(os.path.abspath(__file__))
    suite.addTest(loader.discover(path))
    runner=unittest.TextTestRunner()     #运行器
    runner.run(suite)