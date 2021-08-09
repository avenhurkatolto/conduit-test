# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time


def test_hi():
    # Use a breakpoint in the code line below to debug your script.

    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=chrome_options)
    driver.get('http://www.google.com/')
    time.sleep(5)  # Let the user actually see something!
    assert driver.current_url == "https://www.google.com/?gws_rd=ssl"
