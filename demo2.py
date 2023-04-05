# @Time :2023-3-30 17:23
# @Author :TK
# @Describe :  打开本地网站页面进行测试,按钮，下拉框，选择框，三种弹窗
import os.path

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select  #select工具类
from selenium.webdriver.support.wait import WebDriverWait

class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Edge()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = 'file:///'+path+'/forms.html'
        self.driver.get(file_path)
        sleep(1)
        print(path)

    '''def test_login(self):
        username = self.driver.find_element(By.ID, 'username')
        username.send_keys('admin')
        pwd = self.driver.find_element(By.ID, 'pwd')
        pwd.send_keys('123')
        sleep(1)
        print(username.get_attribute('value'))
        print(pwd.get_attribute('value'))
        self.driver.find_element(By.ID, 'submit').click()
        self.driver.switch_to.alert.accept()    #处理弹窗
        sleep(1)
        username.clear()
        pwd.clear()
        sleep(1)'''

    '''def test_checkbox(self):
        swimming = self.driver.find_element(By.NAME, 'swimming')
        if not swimming.is_selected():
            swimming.click()
        reading = self.driver.find_element(By.NAME, 'reading')
        if not reading.is_selected():
            reading.click()
        sleep(3)
        self.driver.quit()

    def test_radio(self):
        l=self.driver.find_elements(By.NAME,'gender')
        l[0].click()
        sleep(2)'''

    '''def test_select(self):
        se=self.driver.find_element(By.NAME,'year')
        select=Select(se)
        # select.select_by_index(1)  #根据索引寻找
        # sleep(1)
        # select.select_by_value('2')
        # sleep(1)
        # select.select_by_visible_text('2003')
        # sleep(1)

        # for i in range(3):
        #     select.select_by_index(i)
        #     sleep(1)
        # sleep(3)
        # select.deselect_all()   #反选
        
        # for option in select.options:   #遍历所有option
        #     print(option.text)
        # 
        # self.driver.quit()'''

    '''def test_alert(self):
        self.driver.find_element(By.ID,'alert').click()
        alert=self.driver.switch_to.alert
        print(alert.text)
        sleep(1)
        alert.accept()

    def test_confirm(self):
        self.driver.find_element(By.ID, 'confirm').click()
        confirm = self.driver.switch_to.alert
        print(confirm.text)
        sleep(3)
        confirm.dismiss()   #确认弹窗

    def test_prompt(self):
        self.driver.find_element(By.ID, 'prompt').click()
        sleep(2)
        prompt= self.driver.switch_to.alert
        print(prompt.text)
        sleep(1)
        prompt.accept()'''






if __name__ == '__main__':
    case = TestCase()
    # case.test_login()
    # case.test_checkbox()
    # case.test_radio()
    # case.test_select()
    # case.test_alert()
    # case.test_confirm()
    case.test_prompt()