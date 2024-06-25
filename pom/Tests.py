from keyboard import press
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class LoginProcess:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def super_login(self):
        self.driver.get("http://192.168.20.127/UltimusFinSolutionTest/UFS.Web/")
        time.sleep(1)
        # User id
        user_id_input = self.driver.find_element(By.XPATH, "//input[@id='UserId']")
        user_id_input.send_keys('Jesan100')
        time.sleep(1)
        # Password
        password_input = self.driver.find_element(By.XPATH, "//input[@id='PasswordString']")
        password_input.send_keys('1')
        time.sleep(1)
        press("TAB")
        time.sleep(1)
        press("down")
        time.sleep(1)
        press("Enter")
        # Login button
        login_button = self.driver.find_element(By.XPATH, "//button[@id='btnlogin']")
        login_button.click()
        time.sleep(3)

class SMSPath:
    def __init__(self, driver):
        self.driver = driver

    def path_0951(self):
        # Search input
        search_input = self.driver.find_element(By.XPATH, "//input[@id='txtfastpath']")
        search_input.click()
        time.sleep(1)
        search_input.send_keys('0951')
        time.sleep(1)
        # Search button
        search_button = self.driver.find_element(By.XPATH, "//span[@class='glyphicon glyphicon-circle-arrow-right']")
        search_button.click()
        time.sleep(5)

    def user_profile(self):
        # User id input
        user_id_input = self.driver.find_element(By.XPATH, "//input[@id='LoginId']")
        user_id_input.send_keys("e5974")
        time.sleep(1)
        # User profile name input
        user_profile_name_input = self.driver.find_element(By.XPATH, "//input[@name='userProfileName']")
        user_profile_name_input.click()
        time.sleep(2)
        user_profile_name_input.send_keys("hasan")
        time.sleep(3)
        # Bank staff checkbox
        bank_staff_checkbox = self.driver.find_element(By.XPATH, "//input[@id='BankStaff']")
        bank_staff_checkbox.click()
        time.sleep(1)
        # Email input
        email_input = self.driver.find_element(By.XPATH, "//input[@id='UserEmailId']")
        email_input.send_keys("zim@leads-bd.com")
        time.sleep(1)
        # Mobile input
        mobile_input = self.driver.find_element(By.XPATH, "//input[@id='MobileNumber']")
        mobile_input.send_keys('01967360664')
        time.sleep(2)
        # Branch Office dropdown
        branch_dropdown = Select(self.driver.find_element(By.XPATH, "//select[@name='HomeBranchId']"))
        branch_dropdown.select_by_visible_text('MSZ Bank (5974)')
        time.sleep(2)
        # Textarea input
        textarea_input = self.driver.find_element(By.XPATH, "//textarea[@class='form-control ls-control lstextarea ng-pristine ng-untouched ng-empty ng-invalid ng-invalid-required']")
        textarea_input.send_keys('zim')
        time.sleep(2)
        # Any Branch Report Access checkbox
        any_branch_report_checkbox = self.driver.find_element(By.XPATH, "//input[@id='AnyBranchReportAccess']")
        any_branch_report_checkbox.click()
        time.sleep(1)
        # Press down arrow multiple times
        for _ in range(3):
            press('Down')
            time.sleep(1)
        # Add all rows button
        add_all_rows_button = self.driver.find_element(By.XPATH, "//button[@id='addAllRows']")
        add_all_rows_button.click()
        time.sleep(2)
        alert = self.driver.switch_to.alert
        alert.accept()
        time.sleep(2)
        # Click on a button
        button = self.driver.find_element(By.XPATH, "//b[@class='ng-binding']")
        button.click()
        time.sleep(2)

driver = webdriver.Chrome()

login = LoginProcess()
login.super_login()

path = SMSPath(driver)
path.path_0951()
path.user_profile()

driver.quit()
