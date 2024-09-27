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



def firefox_setup_driver():

    firefox_web_driver = webdriver.Firefox(firefox_binary= r"C:\Program Files\Mozilla Firefox\firefox.exe", executable_path='geckodriver.exe' ,) 

    return firefox_web_driver


# if __name__ == "__main__":

#     firefox_driver = firefox_setup_driver()

#     firefox_driver.get("https://amazon.com")