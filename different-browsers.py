from argparse import Action
from ctypes import alignment
import imp
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
import selenium.common.exceptions
import sys
from time import sleep
from driver import setup_driver
from gecko_driver import firefox_setup_driver
from random import randint
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


if __name__ == "__main__":
    chrome_driver = setup_driver()
    chrome_driver.get("https://google.com")
    chrome_driver.quit()

    sleep(5)

    firefox_driver = firefox_setup_driver()
    firefox_driver.get("https://google.com")
    firefox_driver.quit()
