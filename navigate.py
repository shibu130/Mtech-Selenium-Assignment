import imp
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import selenium.common.exceptions
import sys
from time import sleep
from driver import setup_driver

if __name__ == "__main__":

    chrome_driver = setup_driver()

    chrome_driver.get("https://amazon.com")
