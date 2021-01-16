import time
import selenium
import configparser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

c = ('Test Meeting').lower()

#The click function clicks the desired path
def click(path):
    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, path))
        )
        element.click()
    except:
        driver.quit()

#The path to the location where the chromedriver is located at
PATH = "chromedriver.exe"

#Automatically adds the profile 1 user to chrome to prevent any future sign ins after the first time
options = webdriver.ChromeOptions()
#options.add_argument('--user-data-dir=C:\\Users\\logan\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1')
#options.add_argument('--profile-directory=Profile 1')

driver = webdriver.Chrome(executable_path=PATH, options=options)

# Parse ini file
config = configparser.ConfigParser()
config.read("config.ini")

#The driver obtains the path to the website (Microsoft Teams)
driver.get(config["Login"]["MeetingLink"])

#Wait for the website to load in
time.sleep(5)

user_path = "/html/body/div/form[1]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/input[1]"
pass_path = "/html/body/div/form[1]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/input"

click(user_path)
driver.find_element_by_xpath(user_path).send_keys(config["Login"]["Name"])
click("/html/body/div/form[1]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div/div[4]/div/div/div/div/input")

# go next
exit = False
while not exit:
  try:
    click(pass_path)
    driver.find_element_by_xpath(pass_path).send_keys(config["Login"]["Password"])
    exit = True
  except:
    pass

# Sign in
click("/html/body/div/form[1]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[3]/div[2]/div/div/div/div/input")


#The while loop loops through the first page of classes (the active classes) and clicks on the desired class
i = 0
end = False


while end != True:
    i += 1
    element = driver.find_element_by_xpath('''//*[@id="chatstab"]/div/div/chat-list-bridge/div/div[1]/div/ul/li/div[2]/div[%s]/a''' % (i))
    print (element.get_attribute('title'))
    if i % 29 == 0:
        click('''//*[@id="chatstab"]/div/div/chat-list-bridge/div/div[1]/div/ul/li/div[2]/div[%s]/a''' % (i))
    if element.get_attribute('title').lower() == c:
        click('''//*[@id="chatstab"]/div/div/chat-list-bridge/div/div[1]/div/ul/li/div[2]/div[%s]/a''' % (i))
        end = True

click('''//*[@id="app-messages-header"]/ng-include/chat-header/div/div[3]/button[1]''')
try:
    time.sleep(3)
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[2]/toggle-button[1]'))
    )
    if element.get_attribute('title') == 'Turn camera off':
        element.click()
except:
    driver.quit()


try:
    time.sleep(3)
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.XPATH,'//*[@id="preJoinAudioButton"]'))
    )
    if element.get_attribute('title') == 'Mute microphone':
        element.click()
except:
    driver.quit()

click('''//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div/button''')

time.sleep(5)
driver.quit()

#Find a way to loop through website's chat bar's Xpath
#Use the xpath and return the title associated with it
#If the title == the desired class's title's Xpath
#Then you enter the class





