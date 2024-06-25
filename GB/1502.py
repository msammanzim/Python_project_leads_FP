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

driver.find_element(By.XPATH,value="//input[@id='txtMenuSearch']").send_keys('1502')
time.sleep(1)
press('Enter')

#Trade Name by useing his name

driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtName']").send_keys('RATUL')
time.sleep(1)

#Basic Info:-----------

#Organization Type ID (CB) Drop_Down List:

driver.find_element(By.XPATH,value="//select[@id='ctl00_contPlcHdrMasterHolder_LstxtIDCBORG']").click()
time.sleep(1)
press('down')
time.sleep(1)
press('down')
time.sleep(1)
press('enter')

#E-Tin Mandatory Field to Change and contais 12 desit @:

driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtTIN_E_ORG']").send_keys('699245595236')
time.sleep(1)

#Introducer Type Drop_down Lsit :
driver.find_element(By.XPATH,value="//select[@id='ctl00_contPlcHdrMasterHolder_LsddlIntroducerType']").click()
press('down')
time.sleep(1)
press('down')
time.sleep(1)
press('down')
press('enter')
time.sleep(1)


#Click Organization Details:--------

driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_TabCIFOrgDtlInfo']").click()
time.sleep(1)

#Vat Reg need to change max limit 20 digit @

driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtVATRegistrationNo']").send_keys('5518325')
time.sleep(1)

#BOI Reg number need to change max limit 20 digit @

driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtBOIregNo']").send_keys('5783995')
time.sleep(1)

#Business Identification No need to chnage max limit 20 digit @

driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtBusinessIdentificationNo']").send_keys('399525591552')
time.sleep(1)
press('down')

#Date of Incorporation change based on bank date ##/##/####

driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtDOE']").send_keys('10/09/2023')
time.sleep(1)

#Owner/shareholder info need 2 time same click :----------
driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_TabOwnrShrInfo']").click()
time.sleep(1)
driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_TabOwnrShrInfo']").click()
time.sleep(1)

#Owner Customer ID have to change if need ##

driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtOWNER_CUST_ID']").send_keys('0000875939')
time.sleep(1)

#Organization Type drop_down:

driver.find_element(By.XPATH,value="//select[@id='ctl00_contPlcHdrMasterHolder_lsddlOrganizationType']").click()
time.sleep(1)
driver.find_element(By.XPATH,value="//select[@id='ctl00_contPlcHdrMasterHolder_lsddlOrganizationType']").click()
press('down')
time.sleep(1)
press('down')
time.sleep(1)
press('enter')
time.sleep(1)

#Role/Designation Code drop_down:

driver.find_element(By.XPATH,value="//select[@id='ctl00_contPlcHdrMasterHolder_LsddlDesignationCode']").click()
press('down')
time.sleep(1)
press('down')
time.sleep(1)
press('enter')
time.sleep(1)

#Owners Share (%)

driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtShare']").send_keys(60)
time.sleep(1)

#Resolution Date need to chaneg base on bank date ##/##/####
driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtResolutionDt']").send_keys('10/09/2023')
time.sleep(1)

#click Add for owner Add
driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_btnOwnerAdd']").click()
time.sleep(1)
driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_btnOwnerAdd']").click()
time.sleep(1)

#Owner Customer ID need to chage if need @

driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtOWNER_CUST_ID']").send_keys('0000875943')
time.sleep(1)

#Organization Type Drop_down list:

driver.find_element(By.XPATH,value="//select[@id='ctl00_contPlcHdrMasterHolder_lsddlOrganizationType']").click()
time.sleep(1)
driver.find_element(By.XPATH,value="//select[@id='ctl00_contPlcHdrMasterHolder_lsddlOrganizationType']").click()
press('down')
time.sleep(1)
press('down')
time.sleep(1)
press('enter')
time.sleep(1)

#Role/Designation Code drop_down list:

driver.find_element(By.XPATH,value="//select[@id='ctl00_contPlcHdrMasterHolder_LsddlDesignationCode']").click()
press('down')
time.sleep(1)
press('down')
time.sleep(1)
press('enter')
time.sleep(1)

#Owners Share (%)
driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtShare']").send_keys(40)
time.sleep(1)

#Resolution Date need to change based on the bank date ##/##/####
driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtResolutionDt']").send_keys('10/09/2023')
time.sleep(1)

#click Add

driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_btnOwnerAdd']").click()
time.sleep(1)
driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_btnOwnerAdd']").click()
time.sleep(1)
driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_TabCIFAddress']").click()
time.sleep(1)

#Address Part :---------
driver.find_element(By.XPATH,value="//select[@id='ctl00_contPlcHdrMasterHolder_LsddlCusAddrType']").click()
press('down')
time.sleep(1)
press('enter')
time.sleep(1)

#Address

driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtCusAddress1']").send_keys('Dhaka')
time.sleep(1)

#city/town/area

driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtCusTown']").send_keys('Dhaka')
time.sleep(1)

#Zip Code

driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtCusPostCode']").send_keys('5268')
time.sleep(1)

#Mobile

driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtCusMobile']").send_keys('01967360664')

#Click add

driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_btnAddressAdd']").click()
time.sleep(1)
driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_btnAddressAdd']").click()
time.sleep(1)
#Schroll
driver.find_element(By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(1)
driver.find_element(By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(1)
driver.find_element(By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(1)
driver.find_element(By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(1)

#Trade info:------------

driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_TabCIFTrade']").click()
time.sleep(1)
time.sleep(1)


#tred license mendatory field need to chnage @

driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtTradeLicenseNo']").send_keys('69987935')
time.sleep(2)

#Trade License Issue Date

driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtTradeLicenseIssueDate']").click()
time.sleep(1)
driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtTradeLicenseIssueDate']").send_keys('10/09/2023')
time.sleep(2)

#Trade License Expiry Date

driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtTradeLicenseExpiryDate']").click()
time.sleep(1)
driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtTradeLicenseExpiryDate']").send_keys('10/09/2030')
time.sleep(2)

#Trade License Renewal Date From

driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtTrdLicRenewDtFrom']").click()
time.sleep(1)
driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtTrdLicRenewDtFrom']").send_keys('10/09/2023')
time.sleep(2)

#Trade License Renewal Date To

driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtTrdLicRenewDtTo']").click()
time.sleep(1)
driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtTrdLicRenewDtTo']").send_keys('10/09/2030')
time.sleep(2)

#Address

driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtTRddress']").click()
time.sleep(1)
driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtTRddress']").send_keys('Dhaka')
time.sleep(1)

#City

driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtTRCity']").send_keys('Dhaka')
time.sleep(1)

#zip

driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtTRZip']").send_keys('8568')
time.sleep(1)
press('down')
press('down')
time.sleep(1)
press('down')
time.sleep(1)
driver.find_element(By.ID,value="ctl00_contPlcHdrMasterHolder_LschkImporter").click()
time.sleep(2)
press('down')
time.sleep(1)
press('down')
time.sleep(1)
press('down')
press('down')
press('down')
time.sleep(1)

#IRC Information

driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtIRCNo']").click()
time.sleep(1)

#IRC No

driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtIRCNo']").send_keys('546542565')
time.sleep(2)

#IRC Issue Date

driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtIRCIssueDate']").click()
time.sleep(1)
driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtIRCIssueDate']").send_keys('10/09/2023')
time.sleep(1)

#IRC Validate Date:

driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtIRCExpiryDate']").click()
time.sleep(1)
driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtIRCExpiryDate']").send_keys('10/09/2030')
time.sleep(2)
press('down')
time.sleep(1)
press('down')
time.sleep(1)

#Importer Type drop_down

driver.find_element(By.XPATH,value="//select[@id='ctl00_contPlcHdrMasterHolder_LsddlIRCType']").click()
time.sleep(1)
press('down')
time.sleep(1)
press('enter')
time.sleep(1)

driver.find_element(By.XPATH,value="//select[@id='ctl00_contPlcHdrMasterHolder_LsddlIRCType']").click()
time.sleep(1)
press('down')
time.sleep(1)
press('enter')
time.sleep(1)

#IRC LIMIT

driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtIRCLimit']").send_keys('500000')
time.sleep(1)
press('down')
time.sleep(1)
press('down')

#ERC Information

driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LsChkExporter']").click()
time.sleep(1)
driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtERCNo']").click()
time.sleep(1)

#ERC No

driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtERCNo']").send_keys('55682485')
time.sleep(1)
driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LsChkExporter']").click()
time.sleep(1)

#ERC date

driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LsChkExporter']").send_keys('10/09/2023')
time.sleep(1)
driver.find_element(By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(1)
driver.find_element(By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(1)
driver.find_element(By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(1)
driver.find_element(By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(1)

#EDF Information

driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LschkEDFInformation']").click()
time.sleep(1)
driver.find_element(By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(1)
driver.find_element(By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(1)
driver.find_element(By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(1)
driver.find_element(By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(1)

driver.find_element(By.XPATH,value="//select[@id='ctl00_contPlcHdrMasterHolder_LsddlBranchCurrency']").click()
time.sleep(1)
press('down')
time.sleep(1)
press('down')
time.sleep(1)
press('enter')
time.sleep(1)
driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtTotalEDFLimit']").click()
time.sleep(1)
driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtTotalEDFLimit']").send_keys('50000')
time.sleep(1)
driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtIssueDate']").click()
time.sleep(1)
driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtIssueDate']").send_keys('10/09/2023')
time.sleep(1)
driver.find_element(By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(1)
driver.find_element(By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(1)
driver.find_element(By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(1)
driver.find_element(By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(1)
driver.find_element(By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(1)
driver.find_element(By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(1)
driver.find_element(By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(1)
driver.find_element(By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(1)
driver.find_element(By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(1)
driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtExpiryDate']").click()
time.sleep(1)
driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_LstxtExpiryDate']").send_keys('10/09/2030')
time.sleep(5)

#KYC Information:-----------

driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_TabOrgKYC']").click()
time.sleep(1)
driver.find_element(By.XPATH,value="//input[@id='ctl00_contPlcHdrMasterHolder_TabOrgKYC']").click()
time.sleep(1)
driver.find_element(By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(1)
driver.find_element(By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(1)
driver.find_element(By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(1)
driver.find_element(By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(1)
driver.find_element(By.TAG_NAME,value="body").send_keys(Keys.PAGE_DOWN)
time.sleep(1)
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
time.sleep(2)

driver.save_screenshot("last_page.png")
time.sleep(10)



