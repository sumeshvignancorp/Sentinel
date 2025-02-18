from datetime import datetime

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

from webdriver_manager.chrome import ChromeDriverManager


@allure.description("Verify adding a driver by entering the name and phone details in the Add Driver page.")
def test_add_driver():
    chrome_options = Options()
    chrome_options.debugger_address = "localhost:9222"
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://sentinel-live.co.uk")
    time.sleep(10)

    # Driver = 1
    driver.find_element("xpath", "(//div[@role='button'])[7]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[text()='Drivers']").click()
    time.sleep(2)
    driver.find_element("xpath", "(//button[@type='button'])[22]").click()
    time.sleep(2)
    driver.find_element("xpath", "(//input[@type='text'])[1]").send_keys("TestDriver")
    driver.find_element("xpath", "(//input[@type='text'])[2]").send_keys(generate_Identifier())
    driver.find_element("xpath", "(//input[@type='text'])[3]").send_keys("9645673443")
    driver.find_element("xpath", "//button[text()='Save']").click()
    time.sleep(1)
    driver.get_screenshot_as_file("../Results&Status/12Driver added.png")
    time.sleep(5)

    # delete
    driver.find_element("xpath", "(//button[@type='button'])[21]").click()
    driver.find_element("xpath", "//button[text()='Yes']").click()
    driver.get_screenshot_as_file("../Results&Status/13Driver Delete.png")
    print('Add/Delete Driver Passed and Captured')
    print("URL of the page:", driver.current_url)
    time.sleep(1)
    driver.quit()


def generate_Identifier():
    time_stamp = datetime.now().strftime("%d%M%S")  # "%Y_%m_%d_%H_%M_%S"
    return "KA01XY" + time_stamp
