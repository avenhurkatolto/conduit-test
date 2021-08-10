import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

def test_deletedata():

    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')

    name = "user33"
    email = name + "@hotmail.com"
    pw = "Userpass1"

    driver = webdriver.Chrome(options=chrome_options)

    driver.get("http://localhost:1667/#/login")
    time.sleep(3)
    driver.find_element_by_css_selector("#app > div > div > div > div > form > fieldset:nth-child(1) > input").send_keys(email)
    driver.find_element_by_css_selector("#app > div > div > div > div > form > fieldset:nth-child(2) > input").send_keys(pw)
    driver.find_element_by_css_selector("#app > div > div > div > div > form > button").click()

    time.sleep(3)

    driver.get("http://localhost:1667/#/editor")
    time.sleep(3)
    # app > div > div > div > div > form > fieldset > fieldset:nth-child(1) > input
    driver.find_element_by_css_selector("#app > div > div > div > div > form > fieldset > fieldset:nth-child(1) > input").clear()
    driver.find_element_by_css_selector("#app > div > div > div > div > form > fieldset > fieldset:nth-child(1) > input").send_keys("Title99")
    driver.find_element_by_css_selector("#app > div > div > div > div > form > fieldset > fieldset:nth-child(2) > input").send_keys("Subtitle1")
    driver.find_element_by_css_selector("#app > div > div > div > div > form > fieldset > fieldset:nth-child(3) > textarea").send_keys("Message")

    driver.find_element_by_css_selector("#app > div > div > div > div > form > fieldset > fieldset:nth-child(4) > div > div > ul > li > input").send_keys("Testtag")
    driver.find_element_by_css_selector("#app > div > div > div > div > form > fieldset > fieldset:nth-child(4) > div > div > ul > li > input").send_keys(Keys.RETURN)
    driver.find_element_by_css_selector("#app > div > div > div > div > form > button").click()
    time.sleep(3)

    driver.find_element_by_css_selector("#app > div > div.banner > div > div > span > button").click()
    time.sleep(3)
    assert driver.current_url == "http://localhost:1667/#/"