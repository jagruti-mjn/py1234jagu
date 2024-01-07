
from selenium import webdriver
from selenium.webdriver.common.by import By
def test_open_login():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    button = driver.find_element(By.ID,"btn-make-appointment")
    button.click()
