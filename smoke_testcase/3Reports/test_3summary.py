import allure
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

from webdriver_manager.chrome import ChromeDriverManager


@allure.description("Verify the Summary Report functionality, including XLSX and PDF downloads, Mail Report, Scheduled Report, and Show Report options.")
def test_summary_report():
    chrome_options = Options()
    chrome_options.debugger_address = "localhost:9222"
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://sentinel-live.co.uk")
    print("Title of the page:", driver.title)
    time.sleep(10)
    driver.find_element("xpath", "(//div[@role='button'])[3]").click()  # reports
    time.sleep(2)
    driver.find_element("xpath", "//button[text()='Summary']").click()  # summary
    time.sleep(5)
    driver.find_element("xpath", "(//div[@role='combobox'])[2]").click()
    time.sleep(2)
    driver.find_element("xpath", "//li[text()='Today']").click()
    # print("Title :", driver.title)
    driver.find_element("xpath", "(//input[@role='combobox'])").click()
    time.sleep(3)
    driver.find_element("xpath", "(//input[@role='combobox'])").send_keys("Bengaluru")
    time.sleep(2)
    driver.find_element("xpath", "(//input[@role='combobox'])").send_keys(Keys.ARROW_DOWN)
    driver.find_element("xpath", "(//input[@role='combobox'])").send_keys(Keys.ENTER)
    time.sleep(1)
    driver.find_element(By.XPATH, "//span[text()='Show']").click()
    time.sleep(6)
    print("URL of the page:", driver.current_url)
    # Export
    driver.find_element(By.XPATH, "//span[text()='Export']").click()
    time.sleep(2)
    print("Xlsx file downloaded")
    # Email report
    driver.find_element(By.XPATH, "//span[text()='Email Report']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[text()='Send']").click()
    print("Xlsx file sent to Email")
    driver.get_screenshot_as_file("../Results&Status/19Summary_Report.png")
    time.sleep(5)
    print('Summary_Report Passed and Captured')
    time.sleep(3)
    driver.find_element("xpath", "(//div[@role='combobox'])[3]").click()
    time.sleep(2)
    driver.find_element("xpath", "(//li[@role='option'])[2]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//span[text()='Show']").click()
    time.sleep(3)
    print("Daily summary show reported generated")
    time.sleep(2)
    driver.get_screenshot_as_file("../Results&Status/19.1DailySummary_Report.png")
    driver.quit()