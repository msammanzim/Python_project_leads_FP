from keyboard import press
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
from selenium.webdriver.support.ui import Select
from selenium.webdriver import Keys
import time

class login_Process():
    def super_login(self):
        driver.get("http://192.168.20.127/UltimusFinSolutionTest/UFS.Web/")
        time.sleep(1)
        driver.maximize_window()
        # user id
        driver.find_element(By.XPATH, value="//input[@id='UserId']").send_keys('Jesan100')
        time.sleep(1)
        # password
        driver.find_element(By.XPATH, value="//input[@id='PasswordString']").send_keys('1')
        time.sleep(1)
        press("TAB")
        time.sleep(1)
        press("down")
        time.sleep(1)
        press("Enter")
        # login1
        driver.find_element(By.XPATH, value="//button[@id='btnlogin']").click()
        time.sleep(3)

class sms_path():
    def path0957(self):
        #search
        driver.find_element(By.XPATH,value="//input[@id='txtfastpath']").click()
        time.sleep(1)
        # search
        driver.find_element(By.XPATH,value="//input[@id='txtfastpath']").send_keys('0957')
        time.sleep(1)
        # search
        driver.find_element(By.XPATH,value="//span[@class='glyphicon glyphicon-circle-arrow-right']").click()
        time.sleep(5)

    def userid(self):
        driver.find_element(By.XPATH,value="//input[@name='LoginId']").click()
        driver.find_element(By.XPATH,value="//input[@name='LoginId']").send_keys("a3224")
        time.sleep(1)
        driver.find_element(By.XPATH,value="//span[@id='spanUserIdList']").click()
        time.sleep(2)
        driver.find_element(By.XPATH,value="//button[@id='addAllRows']").click()
        time.sleep(2)
        # driver.find_element(By.XPATH,value="").click()
        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(2)
        driver.find_element(By.XPATH,value="//b[@class='ng-binding']").click()
        time.sleep(2)
        





login=login_Process()
login.super_login()
path=sms_path()
path.path0957()
path.userid()



