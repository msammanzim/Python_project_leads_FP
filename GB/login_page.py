import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def login():
    driver = webdriver.Chrome()
    driver.get("http://192.168.20.127/UltimusFinSolutionTest/UFS.Web/")
    driver.maximize_window()

    user_id_input = driver.find_element(By.XPATH, "//input[@id='UserId']")
    user_id_input.send_keys("a5980")
    time.sleep(2)

    password_input = driver.find_element(By.XPATH, "//input[@id='PasswordString']")
    password_input.send_keys("a1")
    time.sleep(2)

    login_button = driver.find_element(By.XPATH, "//button[@id='btnlogin']")
    login_button.click()
    time.sleep(3)

    # Add further actions here after logging in, or return the driver if needed
    return driver

if __name__ == "__main__":
    driver = login()
    # Add further actions here after logging in, or quit the driver if needed
    driver.quit()
