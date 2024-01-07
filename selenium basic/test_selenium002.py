import pytest
from selenium import webdriver

@pytest.fixture()
def driver():
    driver=webdriver.Cyhrome()
    yield driver
#yield/retuen both are same-->value storeis parmanant extra variable

def test_open_url_verify_title(driver):
    driver.get("https://omayo.blogspot.com/")
    print((driver.title))
