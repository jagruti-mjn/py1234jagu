# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
# def test_open_login():
#  driver=webdriver.Chrome()
#  driver.get("https://katalon-demo-cura.herokuapp.com/")
#  driver.maximize_window()
#  make_appointment_btn = driver.find_element(By.ID,'btn-make-appointment')
#  make_appointment_btn.click()
#  time.sleep(20)

import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

def test_open_login():
    driver: WebDriver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()

    make_appointment_btn = driver.find_element(By.ID, 'btn-make-appointment')
    make_appointment_btn.click()

    time.sleep(2)
    print(driver.current_url)
    assert driver.current_url=="https://katalon-demo-cura.herokuapp.com/profile.php#login","Error"

    driver.find_element(By.NAME,'username').send_keys("John Doe")
    time.sleep(2)
    driver.find_element(By.NAME,"password").send_keys("ThisIsNotAPassword")
    time.sleep(2)
    driver.find_element(By.ID,"btn-login").click()

    time.sleep(6)
    driver.find_element(By.ID,"combo_facility").send_keys("Seoul CURA Healthcare Center")
    time.sleep(2)
    driver.find_element(By.ID,"chk_hospotal_readmission").click()
    time.sleep(2)
    driver.find_element(By. ID,"radio_program_medicare").click()
    time.sleep(2)
    driver.find_element(By.ID,"txt_visit_date").click()
    time.sleep(2)
  #  driver.find_element( By.ID).click()
    driver.find_element(By.XPATH,'/html/body/div/div[1]/table/tbody/tr[3]/td[4]')
    time.sleep(2)
    driver.find_element(By.ID,"btn-book-appointment" ).click()
    time.sleep(2)

    # Use an explicit wait to wait for the page to load
    # wait = WebDriverWait(driver, 20)
    # wait.until(EC.title_contains("CURA Healthcare Service"))

    # Add more actions on the new page if needed

    # Close the browser
    # driver.quit()

# Call the function to run the test
test_open_login()
