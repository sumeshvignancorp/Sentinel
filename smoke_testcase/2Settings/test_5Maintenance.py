import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

from webdriver_manager.chrome import ChromeDriverManager


@allure.description("Verify adding maintenance by selecting the maintenance type and entering the odometer reading in the Add Maintenance page.")
def test_add_maintenance():
    chrome_options = Options()
    chrome_options.debugger_address = "localhost:9222"
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://sentinel-live.co.uk")
    time.sleep(10)

    # Maintenance = 1
    driver.find_element("xpath", "(//div[@role='button'])[7]").click()
    time.sleep(2)
    driver.find_element("xpath", "//button[text()='Maintenance']").click()
    time.sleep(2)
    driver.find_element("xpath", "(//button[@type='button'])[24]").click()
    time.sleep(2)
    driver.find_element("xpath", "(//input[@type='text'])[1]").send_keys("tyre ")
    driver.find_element("xpath", "(//div[@role='combobox'])[1]").click()
    driver.find_element("xpath", "(//li[@role='option'])[2]").click()
    time.sleep(2)
    driver.find_element("xpath", "(//input[@type='text'])[2]").send_keys("15001")
    driver.find_element("xpath", "(//input[@type='text'])[3]").send_keys("300")
    time.sleep(3)
    driver.find_element("xpath", "//button[text()='Save']").click()
    time.sleep(1)
    driver.get_screenshot_as_file("../Results&Status/14Maintenance added.png")
    time.sleep(3)

    # delete
    driver.find_element("xpath", "(//button[@type='button'])[23]").click()
    driver.find_element("xpath", "//button[text()='Yes']").click()
    time.sleep(1)
    driver.get_screenshot_as_file("../Results&Status/15Maintenance delete.png")
    print('Add/Delete Maintenance Passed and Captured')
    print("URL of the page:", driver.current_url)
    time.sleep(1)
    driver.quit()
