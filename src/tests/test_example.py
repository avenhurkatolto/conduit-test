# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from selenium import webdriver

import time


def test_hi():
    # Use a breakpoint in the code line below to debug your script.

    driver = webdriver.Chrome()
    driver.get('http://www.google.com/')
    time.sleep(5)  # Let the user actually see something!
    assert driver.current_url == "https://www.google.com/?gws_rd=ssl"
