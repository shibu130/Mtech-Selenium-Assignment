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



def setup_driver():

    webdriver_options = Options()

    webdriver_options.add_argument('--no-proxy-server')

    webdriver_options.binary_location=r"C:\Program Files\Google\Chrome\Application\chrome.exe"

    chrome_web_driver = webdriver.Chrome(chrome_options = webdriver_options, executable_path='chromedriver.exe' ,) 

    return chrome_web_driver


# if __name__ == "__main__":

#     chrome_driver = setup_driver()

#     chrome_driver.get("https://amazon.com")