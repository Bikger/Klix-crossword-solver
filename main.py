import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def solve_krizaljka():
    driver = webdriver.Firefox()
    driver.implicitly_wait(1)
    driver.get("https://www.klix.ba/krizaljka")

    print("Report: ")
    sleep(1)
    try:
        boxes = driver.find_elements(By.XPATH, "//input[@type='text'][@class='polje border-none text-center text-sm md:text-3xl lg:text-4xl font-semibold w-full h-full bg-transparent uppercase js-bound']")
    except:
        print("Boxes not found")

    for code in boxes:
        key = code.get_attribute("data-value")
        code.send_keys(key)
        print(key)

    final_boxes = driver.find_elements(By.XPATH, "//input[@class='polje border-none text-center text-sm md:text-3xl lg:text-4xl font-semibold  w-full h-full bg-transparent uppercase js-bound']")
    for code in final_boxes:
        key = code.get_attribute("data-value")
        code.send_keys(key)
        print(key)

    sleep(2)

    #driver.quit()
    unixTimeStamp = time.time()
    print(unixTimeStamp)
    print("No issues encountered. ")

solve_krizaljka() 
