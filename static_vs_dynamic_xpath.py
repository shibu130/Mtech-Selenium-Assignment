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

    # static xpath
    # at this point of time this when someone would be viewing this thing this XPATH Below would be collapsing
    # that is the problem with the static xpath - someone makes changes to elements add (classes or id or tag or attribute) / delete / edit
    # someone updates and replaces (class , attribute, id , tag)
    chrome_webdriver.find_element(By.XPATH, "/html/body/div[@id='a-page']/header[@id='navbar-main']/div[@id='navbar']/div[@id='nav-belt']/div[@class='nav-left']/div[@id='nav-global-location-slot']/span[@id='nav-global-location-data-modal-action']/a[@id='nav-global-location-popover-link']/div[@id='glow-ingress-block']/span[@id='glow-ingress-line1']")

    sleep(5)

    # dynamic xpath 
    # there is no issue while while using dynamic path since we will not be parsing from top to down
    # we can target a node and also traverse child ancestor or back forth
    chrome_webdriver.find_element(By.XPATH, "//span[@id = 'glow-ingress-line1']")

