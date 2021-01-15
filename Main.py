import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
c = 'SCH4U0C Teams Meeting Link'.lower()

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
PATH = "D:\🐧\Coding stuff\Python files\chromedriver.exe"

#Automatically adds the profile 1 user to chrome to prevent any future sign ins after the first time
options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=C:\\Users\\logan\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1')
options.add_argument('--profile-directory=Profile 1')

driver = webdriver.Chrome(executable_path=PATH, options=options)

#The driver obtains the path to the website (Microsoft Teams)
driver.get("https://teams.microsoft.com/_#/conversations/19:meeting_ZTJhYmIzYjItNjA0NS00NWZlLWI0ODItMDMyYzZmMTU2OGI2@thread.v2?ctx=chat")

#Wait for 10 seconds for the website to load in
time.sleep(5)

#The while loop loops through the first page of classes (the active classes) and clicks on the desired class
i = 0
end = False
element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="chatstab"]/div/div/chat-list-bridge/div/div[1]/div/ul/li/div[2]/div[1]/a'))
    )

while end != True:
    i += 1
    click('''//*[@id="chatstab"]/div/div/chat-list-bridge/div/div[1]/div/ul/li/div[2]/div[%s]/a''' % (i))
    element = driver.find_element_by_xpath('''//*[@id="chatstab"]/div/div/chat-list-bridge/div/div[1]/div/ul/li/div[2]/div[%s]/a''' % (i))
    print (element.get_attribute('title'))
    if element.get_attribute('title').lower() == c:
        click('''//*[@id="chatstab"]/div/div/chat-list-bridge/div/div[1]/div/ul/li/div[2]/div[%s]/a''' % (i))
        end = True



time.sleep(5)
driver.quit()
'''
// * [ @ id = "chatstab"] / div / div / chat - list - bridge / div / div[1] / div / ul / li / div[2] / div[4] / a
// * [ @ id = "chatstab"] / div / div / chat - list - bridge / div / div[1] / div / ul / li / div[2] / div[5] / a

//*[@id="chatstab"]/div/div/chat-list-bridge/div/div[1]/div/ul/li/div[2]/div[5]/a
'''
#Find a way to loop through website's chat bar's Xpath
#Use the xpath and return the title associated with it
#If the title == the desired class's title's Xpath
#Then you enter the class


'''
click('//*[@id="chatstab"]/div/div/chat-list-bridge/div/div[1]/div/ul/li/div[2]/div[2]/a')

click('//*[@id="app-messages-header"]/ng-include/chat-header/div/div[3]/button[1]')     #join button

try:
    time.sleep(5)
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[2]/toggle-button[1]))
    )
    if element.get_attribute('title') == 'Turn camera off':
        element.click()
except:
    driver.quit()

'''




