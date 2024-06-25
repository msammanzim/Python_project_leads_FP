import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from keyboard import press

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

#personal Details :-----------

driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_TabCIFPersonalInfo']").click()
time.sleep(2)

#Gender

driver.find_element(By.XPATH,value="//select[@id='ctl00_contPlcHdrMasterHolder_LsddlGender']").click()
press('down')
time.sleep(1)
press('down')
time.sleep(1)
press('enter')
time.sleep(1)

#Occupation

driver.find_element(By.XPATH,value="//select[@id='ctl00_contPlcHdrMasterHolder_LsddlOccupation']").click()
press('down')
time.sleep(1)
press('down')
time.sleep(1)
press('enter')
time.sleep(1)

#monthly income

driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtMonthlyIncome']").send_keys('50000')

#introduser

driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_TabCIFIntroducer']").click()
time.sleep(1)
driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_TabCIFIntroducer']").click()
time.sleep(1)

#NID

driver.find_element(By.XPATH,value="//select[@id='ctl00_contPlcHdrMasterHolder_LsddlIntroducerType']").click()
press('down')
time.sleep(1)
press('down')
time.sleep(1)
press('down')
time.sleep(1)
press('enter')
time.sleep(1)

#Address:-------------
driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_TabCIFAddress']").click()
time.sleep(2)

#Address Type

driver.find_element(By.XPATH,value="//select[@id='ctl00_contPlcHdrMasterHolder_LsddlCusAddrType']").click()
time.sleep(1)
press('down')
time.sleep(1)
press('enter')
time.sleep(1)

#Address

driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtCusAddress1']").send_keys("Dhaka")
time.sleep(1)

#City

driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtCusTown']").send_keys("Dhaka")
time.sleep(1)

#Zip

driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtCusPostCode']").send_keys('2516')
time.sleep(1)

#Country

driver.find_element(By.XPATH,value="//select[@id='ctl00_contPlcHdrMasterHolder_LsddlCusCountry']").click()
time.sleep(1)
press('enter')
time.sleep(1)

#Division

driver.find_element(By.XPATH,value="//select[@id='ctl00_contPlcHdrMasterHolder_LsddlCusState']").click()
time.sleep(1)
press('down')
time.sleep(1)
press('enter')
time.sleep(1)

#district

driver.find_element(By.XPATH,value="//select[@id='ctl00_contPlcHdrMasterHolder_LsddlCusDistrict']").click()
time.sleep(1)
press('down')
time.sleep(1)
press('enter')
time.sleep(1)

#ps

driver.find_element(By.XPATH,value="//select[@id='ctl00_contPlcHdrMasterHolder_LsddlCusThana']").click()
time.sleep(1)
press('down')
time.sleep(1)
press('enter')
time.sleep(1)

#Phone

driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtCusPhone']").send_keys("01967360664")
time.sleep(1)

#Check Box
driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LsChkAddressCopy']").click()
time.sleep(1)

#Add
driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_btnAddressAdd']").click()
time.sleep(1)

#Family

driver.find_element(By.ID,value="ctl00_contPlcHdrMasterHolder_TabCIFFamily").click()
time.sleep(1)

#Father

driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtPname']").send_keys('Samman')
time.sleep(1)

#Occu

driver.find_element(By.XPATH,value="//select[@id='ctl00_contPlcHdrMasterHolder_LsddlFDOccupation']").click()
time.sleep(1)
press('down')
time.sleep(1)
press('enter')
time.sleep(1)

#Mother

driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtMName']").send_keys("ASD")
time.sleep(1)
driver.find_element(By.XPATH,value="//select[@id='ctl00_contPlcHdrMasterHolder_LsddlMDOccupation']").click()
time.sleep(1)
press('down')
time.sleep(1)
press('enter')
time.sleep(1)


#KYC
driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_TabCIFKYC']").click()
time.sleep(2)

driver.find_element(By.XPATH,value="//select[@id='ctl00_contPlcHdrMasterHolder_LsddlCustomerConcentration']").click()
time.sleep(1)
press('down')
time.sleep(1)
press('enter')

driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtSectorIDSBS']").click()
time.sleep(1)
driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtSectorIDSBS']").send_keys('10000249')
time.sleep(1)
driver.find_element(By.XPATH,value="//select[@id='ctl00_contPlcHdrMasterHolder_LsddlOWNERSHIP_TYPE_ID_CIB']").click()
time.sleep(1)
press('down')
time.sleep(1)
press('enter')
time.sleep(1)
driver.find_element(By.XPATH,value="//select[@id='ctl00_contPlcHdrMasterHolder_LsddlOWNERSHIP_TYPE_ID_CIB']").click()
time.sleep(1)
driver.find_element(By.XPATH,value="//select[@id='ctl00_contPlcHdrMasterHolder_LsddlOWNERSHIP_TYPE_ID_CIB']").click()
time.sleep(1)
press('down')
time.sleep(1)
press('enter')
time.sleep(1)
driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtNOB']").click()
time.sleep(1)
driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtNOB']").send_keys('hello')
time.sleep(1)
driver.find_element(By.XPATH,value="//select[@id='ctl00_contPlcHdrMasterHolder_LsddlKYCProfessionORG']").click()
time.sleep(1)
driver.find_element(By.XPATH,value="//select[@id='ctl00_contPlcHdrMasterHolder_LsddlKYCProfessionORG']").click()
time.sleep(1)
press('down')
time.sleep(1)
press('enter')
time.sleep(1)
driver.find_element(By.XPATH,value="//select[@id='ctl00_contPlcHdrMasterHolder_LsddlOWNERSHIP_TYPE_ID_CTR']").click()
time.sleep(1)
driver.find_element(By.XPATH,value="//select[@id='ctl00_contPlcHdrMasterHolder_LsddlOWNERSHIP_TYPE_ID_CTR']").click()
time.sleep(1)
press('down')
time.sleep(1)
press('enter')
time.sleep(1)
driver.find_element(By.XPATH,value="//textarea[@id='ctl00_contPlcHdrMasterHolder_LstxtSourceOfFund_Org']").click()
time.sleep(1)
driver.find_element(By.XPATH,value="//textarea[@id='ctl00_contPlcHdrMasterHolder_LstxtSourceOfFund_Org']").send_keys('hello')
time.sleep(1)
driver.find_element(By.XPATH,value="//select[@id='ctl00_contPlcHdrMasterHolder_LsddlKYCOpenNatureORG']").click()
time.sleep(1)
press('down')
time.sleep(1)
press('down')
time.sleep(1)
press('enter')
time.sleep(2)
driver.find_element(By.XPATH,value="//select[@id='ctl00_contPlcHdrMasterHolder_LsddlNBRCategory']").click()
time.sleep(1)
driver.find_element(By.XPATH,value="//select[@id='ctl00_contPlcHdrMasterHolder_LsddlNBRCategory']").click()
time.sleep(1)
press('enter')
time.sleep(1)
press('enter')
time.sleep(1)

#Create Customer Click

driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_btnOk']").click()
time.sleep(5)



