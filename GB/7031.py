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

class demand_7031():
    def transection(self):
        # input fast path
        driver.find_element(By.XPATH, value="//input[@id='txtMenuSearch']").send_keys('7031')
        time.sleep(2)
        press('Enter')
        time.sleep(2)
        driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_lschkContra']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtAccNo']").click()
        time.sleep(1)
        driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtAccNo']").send_keys('1111')
        time.sleep(1)
        press('enter')
        time.sleep(3)
        press('enter')
        driver.find_element(By.XPATH,value="//span[@class='ui-button-text']").click()

        time.sleep(5)
        driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxTransAmtCcy']").send_keys(5000)
        time.sleep(2)
        press('enter')
        time.sleep(2)
        driver.find_element(By.XPATH,value="//textarea[@id='ctl00_contPlcHdrMasterHolder_LstxtNarration']").send_keys('Test')
        time.sleep(2)
        driver.find_element(By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        driver.find_element(By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        driver.find_element(By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        driver.find_element(By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtAccNoContra']").click()
        time.sleep(2)
        driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtAccNoContra']").click()
        time.sleep(2)
        press('backspace')
        time.sleep(1)
        press('backspace')
        time.sleep(1)
        press('backspace')
        time.sleep(1)
        press('backspace')
        time.sleep(1)
        driver.find_element(By.XPATH, value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtAccNoContra']").click()
        time.sleep(1)
        driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtAccNoContra']").send_keys(9013)
        press('enter')
        time.sleep(5)
        driver.find_element(By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        driver.find_element(By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        driver.find_element(By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        driver.find_element(By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        driver.find_element(By.XPATH,value="//select[@id='ctl00_contPlcHdrMasterHolder_LsddlTransAmmountContra']").click()
        time.sleep(3)
        press('down')
        time.sleep(1)
        press('enter')
        time.sleep(1)
        driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxTransAmtCcyContra']").send_keys(5000)
        time.sleep(1)
        press('enter')
        driver.find_element(By.XPATH,value="//textarea[@id='ctl00_contPlcHdrMasterHolder_LstxtNarrationContra']").send_keys("test")
        time.sleep(1)
        driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LsbtnAdd']").click()
        time.sleep(5)
        driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_btnOk']").click()
        time.sleep(5)
        print("Fantastic Work")


login = login_Process()
login.super_login()

demand = demand_7031()
demand.transection()
