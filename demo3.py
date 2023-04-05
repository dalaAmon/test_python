# @Time :2023-3-30 20:24
# @Author :TK
# @Describe :鼠标事件，单击，双击，右键,快捷键操作,执行js脚本，截屏
import os.path

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from time import sleep, strftime, time, localtime


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Edge()
        self.driver.maximize_window()
        self.driver.get('http://www.baidu.com')
        # self.driver.get('http://sahitest.com/demo/clicks.htm')
        # sleep(1)

    '''def test_mouse(self):   #双击，单击，右键

        btn = self.driver.find_element(By.XPATH,'/html/body/form/input[2]')
        ActionChains(self.driver).double_click(btn).perform()
        sleep(2)
        btn = self.driver.find_element(By.XPATH, '/html/body/form/input[3]')
        ActionChains(self.driver).click(btn).perform()
        sleep(2)
        btn = self.driver.find_element(By.XPATH, '/html/body/form/input[4]')
        ActionChains(self.driver).context_click(btn).perform()
        sleep(3)

    def test_key(self):   #快捷键：全选，剪切，粘贴，鼠标移动
        self.driver.get('http://www.baidu.com')
        # kw=self.driver.find_element(By.ID,'kw')
        # kw.send_keys('selenium')
        # kw.send_keys(Keys.CONTROL,'a')
        # sleep(2)
        # kw.send_keys(Keys.CONTROL, 'x')
        # sleep(2)
        # kw.send_keys(Keys.CONTROL, 'v')
        sleep(2)

        e=self.driver.find_element(By.LINK_TEXT,'新闻')
        print(e)
        ac=ActionChains(self.driver).move_to_element(e).click().perform()
        sleep(3)'''
    '''def test1(self):   #js弹窗
        self.driver.execute_script("alert('test')")
        sleep(2)
        self.driver.switch_to.alert.accept()

    def test2(self):   #js获取title
        js='return document.title'
        title=self.driver.execute_script(js)
        print(title)

    def test3(self):   #改变边框的颜色
        js='var q = document.getElementById("kw"); q.style.border="2px solid black"'
        self.driver.execute_script(js)
        sleep(3)

    def test4(self):   #滚动到底部
        self.driver.find_element(By.ID, 'kw').send_keys('selenium')
        self.driver.find_element(By.ID, 'su').click()
        sleep(1)
        js='window.scrollTo(0,document.body.scrollHeight)'
        self.driver.execute_script(js)
        sleep(3)'''

    def test5(self):
        self.driver.find_element(By.ID,'kw').send_keys('selenium')
        self.driver.find_element(By.ID,'su').click()
        sleep(2)
        # self.driver.save_screenshot('baidu.png')   #将截屏保存在同级目录下

        st=strftime("%Y-%m-%d-%H-%M-%S",localtime(time()))#以时间来命名截屏
        fime_name=st+'.png'
        # self.driver.save_screenshot(fime_name)

        path=os.path.abspath('screenshot')  #将截屏保存在文件夹中，通常采用这种方式，也是用时间来命名
        file_path=path+'/'+fime_name
        self.driver.get_screenshot_as_file(file_path)





if __name__ == '__main__':
    case=TestCase()
    # case.test_mouse()
    # case.test_key()
    # case.test1()
    # case.test2()
    # case.test3()
    # case.test4()
    case.test5()