from argparse import Action
from ctypes import alignment
import imp
from lib2to3.pgen2 import driver
from threading import Thread
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

    chrome_webdriver = setup_driver()

    #chrome_webdriver.set_network_conditions(latency = 1000 , download_throughput=10, upload_throughput=10)

    # navigate to amazon.in
    chrome_webdriver.get("https://amazon.in")

    wait_time = 10

    # use of sleep here is basically if website takes time
    # and if we try to locate element it would throw exception
    # hence it would make sense to wait until that time by using sleep and hence preventing exceptions
    # webdriverwait can also be used in this case rather than sleep where we can wait
    # based on various conditions
    sleep(wait_time)

    latency_check =  chrome_webdriver.find_element(By.Id,"twotabsearchtextbox")