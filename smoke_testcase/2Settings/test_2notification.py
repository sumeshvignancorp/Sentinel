import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

from webdriver_manager.chrome import ChromeDriverManager


@allure.description("Verify adding a notification by selecting events and a channel in the Add Notification page.")
def test_add_notifications():
    chrome_options = Options()
    chrome_options.debugger_address = "localhost:9222"
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://sentinel-live.co.uk")
    time.sleep(10)

    # Notification = 3
    driver.find_element("xpath", "(//div[@role='button'])[7]").click()
    time.sleep(3)
    driver.find_element("xpath", "(//button[@type='button'])[27]").click()
    time.sleep(2)
    driver.find_element("xpath", "(//div[@role='combobox'])[1]").click()
    actions = ActionChains(driver)
    demo = driver.find_element(By.XPATH, "(//li[text()='Fuel drop'])[1]")
    actions.click(demo).perform()
    time.sleep(1)
    driver.find_element("xpath", "(//div[@role='combobox'])[2]").click()
    time.sleep(2)
    driver.find_element("xpath", "//li[@data-value='mail']").click()
    driver.find_element("xpath", "//li[@data-value='firebase']").click()
    time.sleep(2)
    actions = ActionChains(driver)
    demo = driver.find_element(By.XPATH, "(//button[@type='button'])[7]")
    actions.click(demo).perform()
    time.sleep(2)
    driver.find_element("xpath", "(//input[@type='checkbox'])").click()
    actions = ActionChains(driver)
    demo = driver.find_element(By.XPATH, "//button[text()='Save']")
    actions.click(demo).perform()
    driver.get_screenshot_as_file("../Results&Status/8Add Notification.png")
    time.sleep(2)
    print("Notification added")

    # Delete
    time.sleep(3)
    driver.find_element("xpath", "(//button[@type='button'])[26]").click()
    driver.find_element("xpath", "//button[text()='Yes']").click()
    driver.get_screenshot_as_file("../Results&Status/9Delete Notification.png")
    time.sleep(2)
    print('Add/Delete Notification Passed and Captured')
    print("URL of the page:", driver.current_url)
    time.sleep(1)
    driver.quit()
