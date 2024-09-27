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
from random import randint
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


if __name__ == "__main__":

    chrome_driver = setup_driver()
    chrome_driver.get("https://amazon.in")
    ui_action = ActionChains(chrome_driver)

    WebDriverWait(chrome_driver,30).until(EC.visibility_of_element_located((By.XPATH,'//input[@id="twotabsearchtextbox"][@name="field-keywords"]')))

    # typing on the search box
    address_element = chrome_driver.find_element(By.XPATH, '//input[@id="twotabsearchtextbox"][@name="field-keywords"]')

    ui_action.click(address_element).perform()


    ui_action.send_keys("apple iphone 13").perform()

    sleep(5)

    search_button = chrome_driver.find_element(By.XPATH,"//input[@id='nav-search-submit-button'][@value='Go']")

    ui_action.click(search_button).perform()


    # iphone elements

    product_elements = chrome_driver.find_elements(By.XPATH, '//div[@class="sg-col-inner"]/div[@cel_widget_id]')

    table_content_name = []
    table_content_discount = []
    table_content_origina_price = []

    for i in product_elements:
        ui_action.move_to_element(i).perform()

        device_text = i.text.split("\n")
        increment = 0
        #sponsored text may be present in first index
        # causing the name not to come in first index
        if(device_text[0] == "Sponsored"):
            increment = 1
        else:
            increment = 0

        table_content_name.append(device_text[0  + increment])
        sleep(2)
        # table_content_discount.append(device_text[3 + increment])
        # table_content_origina_price.append(device_text[4])

        #sleep(2)

    final_list = table_content_name 



    figure, axis = plt.subplots()
    figure.patch.set_visible(False)
    axis.axis('off')
    axis.axis('tight')
    # ax.text(0, 0, 'left center','left','left center')

    #create data
    df = pd.DataFrame(final_list, columns=['Iphones'])

    #create table
    table = axis.table(cellText=df.values, colLabels=df.columns, loc='center')

    #display table
    figure.tight_layout()
    plt.show()


    
    