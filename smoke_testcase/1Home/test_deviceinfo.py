import time
from datetime import datetime

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@allure.description("Verify the Add Device page by entering the IMEI and other required details.")
def test_device():
    chrome_options = Options()
    chrome_options.debugger_address = "localhost:9222"
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://sentinel-live.co.uk")
    time.sleep(18)
    driver.get_screenshot_as_png()
    driver.find_element(By.XPATH, "(//div[@tabindex='0'])[10]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "(//div[@role='button'])[11]").click()
    time.sleep(2)
    actions = ActionChains(driver)
    demo = driver.find_element(By.XPATH, "(//div[@role='button'])[12]")
    actions.double_click(demo).perform()
    time.sleep(1)
    driver.save_screenshot("../Results&Status/Deviceinfo.png")
    driver.find_element(By.XPATH, "//button[text()='View All']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[@aria-label='Daily Summary']").click()
    time.sleep(5)
    print("Device Info & Status card displayed")
    print("URL of the page:", driver.current_url)
    time.sleep(3)
    driver.quit()
