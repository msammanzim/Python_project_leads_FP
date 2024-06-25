import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from keyboard import press
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("http://192.168.20.127/UltimusFinSolutionTest/UFS.Web/")
time.sleep(1)
driver.maximize_window()

#user id

driver.find_element(By.XPATH,value="//input[@id='UserId']").send_keys('a5972')
time.sleep(1)

#password

driver.find_element(By.XPATH,value="//input[@id='PasswordString']").send_keys('a1')
time.sleep(1)

#login

driver.find_element(By.XPATH,value="//button[@id='btnlogin']").click()
time.sleep(1)

#1502 Search the Page:

driver.find_element(By.XPATH,value="//input[@id='txtMenuSearch']").send_keys('1501')
time.sleep(5)
press('Enter')

#Trade Name by useing his name

driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtFirstName']").send_keys('Emon')
time.sleep(1)

#Basic Info:-----------

#NID need to change @
driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtNationalID']").send_keys('2154521545215')
time.sleep(1)

#Bate of Birth

driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtApointmentDate']").click()
driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtApointmentDate']").send_keys("10/10/2000")
time.sleep(2)

#place of birth
driver.find_element(By.XPATH,value="//select[@id='ctl00_contPlcHdrMasterHolder_LsddlPlaceOfBirthOfCustomer']").click()
time.sleep(1)
driver.find_element(By.XPATH,value="//select[@id='ctl00_contPlcHdrMasterHolder_LsddlPlaceOfBirthOfCustomer']").click()
press('down')
time.sleep(1)
press('down')
time.sleep(1)
press('enter')
time.sleep(1)

#KYC
driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_TabCIFKYC']").click()
time.sleep(2)
driver.find_element(By.XPATH,value="//select[@id='ctl00_contPlcHdrMasterHolder_LsddlCustomerConcentration']").click()
time.sleep(2)
press("Down")
time.sleep(1)
press("Enter")
time.sleep(2)
element=driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtSectorIDSBS']")
actions = ActionChains(driver)
actions.double_click(element).perform()
time.sleep(2)


# Wait for the pop-up notification bar to appear
popup = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@id='divMainContent']")))

# Find the button within the pop-up (replace 'your_button_xpath' with the actual XPath of the button)
button = popup.find_element(By.XPATH, "//input[@id='btnFind']")

# Click on the button
button.click()


