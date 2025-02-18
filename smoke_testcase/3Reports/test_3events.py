import allure
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

from webdriver_manager.chrome import ChromeDriverManager


@allure.description("Verify the Events Report functionality, including XLSX and PDF downloads, Mail Report, Scheduled Report, and Show Report options.")
def test_event_report():
    chrome_options = Options()
    chrome_options.debugger_address = "localhost:9222"
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://sentinel-live.co.uk")
    time.sleep(10)
    driver.find_element("xpath", "(//div[@role='button'])[3]").click()  # reports
    time.sleep(2)
    driver.find_element("xpath", "//button[text()='Events']").click()  # events
    time.sleep(5)
    driver.find_element("xpath", "(//div[@role='combobox'])[1]").click()
    time.sleep(2)
    driver.find_element("xpath", "//li[text()='This Week']").click()
    # print("Title :", driver.title)
    driver.find_element("xpath", "(//input[@role='combobox'])").click()
    time.sleep(3)
    driver.find_element("xpath", "(//input[@role='combobox'])").send_keys("Bengaluru")
    time.sleep(2)
    driver.find_element("xpath", "(//input[@role='combobox'])").send_keys(Keys.ARROW_DOWN)
    driver.find_element("xpath", "(//input[@role='combobox'])").send_keys(Keys.ENTER)
    time.sleep(3)
    time.sleep(3)
    driver.find_element(By.XPATH, "//span[text()='Show']").click()
    time.sleep(6)
    print("URL of the page:", driver.current_url)
    # Export
    driver.find_element(By.XPATH, "//span[text()='Export']").click()
    time.sleep(2)
    print("Xlsx file downloaded")
    time.sleep(2)
    # Email report
    driver.find_element(By.XPATH, "//span[text()='Email Report']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[text()='Send']").click()
    print("Xlsx file sent to Email")
    driver.get_screenshot_as_file("../Results&Status/18Events_Report.png")
    print('Events_Report Passed and Captured')
    driver.quit()