from keyboard import press
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
from selenium.webdriver import Keys
import time
class login_Process():
    def super_login(self):
        driver.get("http://192.168.20.127/UltimusFinSolutionTest/UFS.Web/")
        time.sleep(1)
        driver.maximize_window()
        # user id
        driver.find_element(By.XPATH, value="//input[@id='UserId']").send_keys('a5972')
        time.sleep(1)
        # password
        driver.find_element(By.XPATH, value="//input[@id='PasswordString']").send_keys('a1')
        time.sleep(1)
        # login1
        driver.find_element(By.XPATH, value="//button[@id='btnlogin']").click()
        time.sleep(3)



    def path(self):
        driver.find_element(By.XPATH, value="//input[@id='txtMenuSearch']").send_keys('2001')
        time.sleep(2)
        press('Enter')
        driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtAccNoPrdId']").click()
        time.sleep(1)
        driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtAccNoPrdId']").send_keys("121")
        time.sleep(2)
        # provide customer id
        driver.find_element(By.XPATH, value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtCustId']").click()
        time.sleep(1)
        driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtCustId']").send_keys("0000876265")
        time.sleep(2)
        driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtAccOpeningPrp']").send_keys("LC")
        time.sleep(2)
        driver.find_element(By.XPATH,value="//select[@id='ctl00_contPlcHdrMasterHolder_LsddlCusMailAddrType']").click()
        press("down")
        time.sleep(1)
        press("enter")
        time.sleep(1)

login=login_Process()
login.super_login()
login.path()