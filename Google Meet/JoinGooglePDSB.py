# Some school boards like PDSB login with Microsoft after entering the email on Google.

import time
import selenium
import configparser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# The click function clicks the desired path
def click(path):
    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, path))
        )
        element.click()
    except:
        driver.quit()

# The path to the location where the chromedriver is located at
PATH = "../chromedriver.exe"

# Automatically adds the profile 1 user to chrome to prevent any future sign ins after the first time
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
  })

driver = webdriver.Chrome(executable_path=PATH, options=options)

# Parse ini file
config = configparser.ConfigParser()
config.read("Google Meet\config.ini")

# Go to login screen first
driver.get("https://accounts.google.com/ServiceLogin?ltmpl=meet&continue=https%3A%2F%2Fmeet.google.com%3Fhs%3D193&_ga=2.50085542.1691597488.1610833439-435450982.1610833439")

user_path = "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input"
pass_path = "/html/body/div/form[1]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/input"
button = "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button"

click(user_path)
driver.find_element_by_xpath(user_path).send_keys(config["Login"]["Name"])
click(button)
time.sleep(10) 
driver.find_element_by_xpath('''/html/body/div/form[1]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/input[1]''').send_keys(config["Login"]["Name"])
click('''/html/body/div/form[1]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div/div[4]/div/div/div/div[2]/input''')
exit = False
while not exit:
  try:
    time.sleep(2)
    click(pass_path)
    driver.find_element_by_xpath(pass_path).send_keys(config["Login"]["Password"])
    click('''/html/body/div/form[1]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[3]/div[2]/div/div/div/div/input''')
    exit = True
  except:
    pass

click('//*[@id="idSIButton9"]')
click('''/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button''')
# google meet is so slow????
code_path = "/html/body/div[1]/c-wiz/div/div/div/div[2]/div[2]/div[2]/div/c-wiz/div[1]/div/div/div[1]"
click(code_path)
driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[2]/span/div/div[2]/div[1]/div[1]/input").send_keys(config["Login"]["Link"] + "\n")

time.sleep(8)
# Disable Camera & Microphone
click("/html/body/div[1]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[3]/div[2]/div/div")
click("/html/body/div[1]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[3]/div[1]/div[1]/div/div[1]")

# Join Call
click("/html/body/div[1]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]")
