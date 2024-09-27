from argparse import Action
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


if __name__ == "__main__":

    chrome_driver = setup_driver()
    chrome_driver.get("https://amazon.in")

    ui_action = ActionChains(chrome_driver)

    #start static textbox

    # wait until amazon loads
    WebDriverWait(chrome_driver,30).until(EC.visibility_of_element_located((By.XPATH,'//input[@id="twotabsearchtextbox"][@name="field-keywords"]')))

    #static address element 
    address_element = chrome_driver.find_element(By.XPATH, '//input[@id="twotabsearchtextbox"][@name="field-keywords"]')

    ui_action.click(address_element).perform()

    sleep(5)

    # click outside element
    click_outside_element = chrome_driver.find_element(By.ID,'nav-cover')

    ui_action.click(click_outside_element).perform()

    sleep(5)

   #end : static textbox
    
   #start : dynamic elements

    #performing search on amazon.in

    address_element = chrome_driver.find_element(By.XPATH, '//input[@id="twotabsearchtextbox"][@name="field-keywords"]')

    ui_action.click(address_element).perform()


    ui_action.send_keys("apple iphone 13").perform()


    # search button 

    search_button = chrome_driver.find_element(By.XPATH,"//input[@id='nav-search-submit-button'][@value='Go']")

    ui_action.click(search_button).perform()

    sleep(3)

    
    # select first product 
    
    product_id = chrome_driver.find_elements(By.XPATH,"//h2/a[@class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']")

    random = randint(0, len(product_id))
    
    ActionChains(chrome_driver).move_to_element(product_id[random]).perform()

    

    ActionChains(chrome_driver).click(product_id[random]).perform()
   # ActionChains(chrome_driver).move_to_element(product_id[randint[0,8]]).perform()

    sleep(5)

    chrome_driver.switch_to.window(chrome_driver.window_handles[0])

       # change filter 

    filter = "s-result-sort-select"

    # wait until the filter renders

    WebDriverWait(chrome_driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//select[@id='s-result-sort-select']")))


    filter_element = chrome_driver.find_element(By.XPATH, "//select[@id='s-result-sort-select']")

    ActionChains(chrome_driver).click(filter_element).perform()

    sleep(5)


   # select a dropdown with value high to low

    dropdown_choice = "a-dropdown-link"


    dropdown_choice_element  =  chrome_driver.find_element(By.LINK_TEXT, 'Price: Low to High')


    ActionChains(chrome_driver).click(dropdown_choice_element).perform()


