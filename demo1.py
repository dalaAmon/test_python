# @Time :2023-3-30 16:32
# @Author :TK
# @Describe :selenium继续学习

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class TestCase(object):
    def __init__(self):
        self.driver=webdriver.Edge()
        self.driver.get('http://sahitest.com/demo/linkTest.htm')
        sleep(1)
        # self.driver.maximize_window()
    def test_webelement_prop(self):
        e=self.driver.find_element(By.ID,'t1')
        print(type(e))
        print(e.tag_name)
        print(e.size)
        print(e.rect)
        print(e.text)

    def test_webelement_method(self):
        e=self.driver.find_element(By.ID,'t1')
        e.send_keys('hello world')
        sleep(1)

        print(e.get_attribute('type'))
        print(e.get_attribute('name'))
        print(e.get_attribute('value'))
        print(e.value_of_css_property('font'))
        print(e.value_of_css_property('color'))
        sleep(2)
        e.clear()


#     def test_prop(self):
#         print(self.driver.name)  #浏览器名称
#         print(self.driver.current_url)  #当前页面的url
#         print(self.driver.title)     #显示title
#         print(self.driver.window_handles)    #获取所有窗口的句柄到当前会话，返回一个窗口句柄列表
#         # print(self.driver.page_source)    #当前标签页浏览器渲染之后的网页源代码
#         self.driver.quit()   #关闭浏览器

#     def test_method(self):
#         self.driver.find_element(By.ID,'kw').send_keys('selenium')
#         self.driver.find_element(By.ID,'su').click()
#         sleep(1)
#         self.driver.back()  #浏览器后退
#         sleep(1)
#         self.driver.refresh()   #浏览器刷新
#         sleep(1)
#         self.driver.forward()  #浏览器前进
#
#         self.driver.close()  #关闭当前的tab

if __name__ == '__main__':
    case=TestCase()
    # case.test_webelement_prop()
    case.test_webelement_method()
#     # case.test_prop()
#     case.test_method()
