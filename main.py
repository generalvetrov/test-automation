from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import os


url = "http://suninjuly.github.io/explicit_wait2.html"

    
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(url)

    price = browser.find_element(By.ID, 'price')
    button = browser.find_element(By.ID, 'book')

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    button.click()

    input = browser.find_element(By.ID, "answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input)
    x_element = browser.find_element(By.ID, "input_value").text
    input.send_keys(calc(x_element))

    submitButton = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submitButton.click()

    time.sleep(10)
    browser.quit()

finally:
    print('done')
