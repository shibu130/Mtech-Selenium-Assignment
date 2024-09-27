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
from time import perf_counter
from driver import setup_driver
from gecko_driver import firefox_setup_driver
from random import randint
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np




if __name__ == "__main__":

    chrome_webdriver = setup_driver()
    ui_action =  ActionChains(chrome_webdriver)

    chrome_webdriver.get("https://amazon.in")


    sleep(5)



    start_xpath = perf_counter()
    element2 = chrome_webdriver.find_element(By.XPATH, "//div[@class='nav-fill']/div/input[@id = 'twotabsearchtextbox']")



    end_xpath = perf_counter()

    sleep(5)




    start_time_css = perf_counter()


    element = chrome_webdriver.find_element(By.ID, "twotabsearchtextbox")
    
    end_time_css = perf_counter()


    sleep(5)
     
    


    
    
    

    



    
    # selenium is not a good tool to measure the time taken to measure how long it takes to find element
    # Xpath would take longer time to find elements because it would take it lot of time to scan dom from start to  finish
    # traversals can be from parent to child and vice versa

    # other selectors would use lesser time since we directly specify what elements we want to find and it can be directly fetched
    #easily and there are no traversals

    

    print("{0} seconds css vs {1} XPATH seconds ".format((end_time_css - start_time_css),(end_xpath - start_xpath)))