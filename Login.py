from argparse import Action
import imp
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


if __name__ == "__main__":

    chrome_webdriver = setup_driver()

    # navigate to amazon.in
    chrome_webdriver.get("https://amazon.in")

    # sleep for 5 seconds for page to load or use 
    

    # wait util the element loaded (if loaded we continue)
    WebDriverWait(chrome_webdriver,30).until(EC.visibility_of_element_located((By.ID, "nav-link-accountList")))
    
    # signin button
    singin_element = chrome_webdriver.find_element(By.ID,"nav-link-accountList")
    
    #print(element) 
    ui_action =  ActionChains(chrome_webdriver)

    # using actionchains to click on the signin button
    ui_action.click(singin_element).perform()

    #username textfield
    user_name_field = "ap_email"

    # wait for the text box to be visible

    WebDriverWait(chrome_webdriver,30).until(EC.visibility_of_all_elements_located((By.XPATH, "//input[@id='ap_email'][@name = 'email']")))


    # text field element
    username_element = chrome_webdriver.find_element(By.XPATH , '//input[@id="ap_email"][@name = "email"]')
    
    # click on username element
    ui_action.click(username_element).perform()

    # write username
    ui_action.send_keys("youremail@gmail.com").perform() 

    sleep(2)

    #continue button
    continue_button_element = chrome_webdriver.find_element(By.XPATH, '//input[@id="continue"][@aria-labelledby="continue-announce"]')

    #click on continue

    ui_action.click(continue_button_element).perform()

    sleep(2)

    WebDriverWait(chrome_webdriver,30).until(EC.visibility_of_element_located((By.XPATH, '//input[@id="ap_password"][@name="password"]')))

    #password element
    password_element = chrome_webdriver.find_element(By.XPATH,'//input[@id="ap_password"][@name="password"]')

    ui_action.click(password_element).perform()

    ui_action.send_keys("yourpassword").perform()



    # final signin button

    final_submit_element = chrome_webdriver.find_element(By.XPATH,'//input[@id="signInSubmit"][@class="a-button-input"]')

    ui_action.click(final_submit_element).perform()


    sleep(10)

    chrome_webdriver.quit()