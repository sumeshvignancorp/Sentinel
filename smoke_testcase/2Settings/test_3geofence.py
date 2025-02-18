import allure
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@allure.description("Verify adding a geofence with any area on the map, including a name and other details in the Add Geofence page.")
def test_add_geofence():
    chrome_options = Options()
    chrome_options.debugger_address = "localhost:9222"
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://sentinel-live.co.uk")
    time.sleep(6)

    # Geofence = 1
    driver.find_element("xpath", "(//div[@role='button'])[7]").click()
    time.sleep(4)
    driver.find_element(By.XPATH, "//button[text()='Geofences']").click()
    time.sleep(5)
    driver.find_element("xpath", "(//span[@aria-hidden='true'])[4]").click()
    time.sleep(10)
    driver.find_element("xpath", "//button[@title='Marker tool (m)']").click()
    time.sleep(5)
    actions = ActionChains(driver)
    demo = driver.find_element(By.XPATH, "//canvas[@role='region']")
    actions.click(demo).perform()
    time.sleep(6)
    driver.find_element("xpath", "(//input[@type='text'])[1]").send_keys("Test_Location")
    time.sleep(3)
    driver.find_element("xpath", "//button[text()='Save']").click()
    time.sleep(2)
    driver.get_screenshot_as_file("../Results&Status/10Add Geofence.png")
    time.sleep(3)

    # delete
    time.sleep(3)
    driver.find_element("xpath", "(//div[@role='button'])[11]").click()
    time.sleep(4)
    driver.find_element("xpath", "(//button[@type='button'])[14]").click()
    driver.find_element("xpath", "//button[text()='Yes']").click()
    time.sleep(1)
    driver.get_screenshot_as_file("../Results&Status/11Delete Geofence.png")
    time.sleep(1)
    print('Add/Delete Geofence Passed and Captured')
    print("URL of the page:", driver.current_url)
    time.sleep(2)
    driver.quit()
