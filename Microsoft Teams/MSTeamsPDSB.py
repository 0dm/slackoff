import time

import selenium
import configparser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

c = ('Test Meeting').lower()


# The click function clicks the desired path
def click(path):
    e = False
    while not e:
        try:
            ele = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, path))
            )
            ele.click()
            e = True
        except:
            pass


# The path to the location where the chromedriver is located at
PATH = "chromedriver.exe"

# Automatically adds the profile 1 user to chrome to prevent any future sign ins after the first time
options = webdriver.ChromeOptions()
options.add_argument("--disable-default-apps")
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
})
options.add_argument('--lang=en-US')
driver = webdriver.Chrome(executable_path=PATH, options=options)

# Parse ini file
config = configparser.ConfigParser()
config.read("config.ini")

# The driver obtains the path to the website (Microsoft Teams)
driver.get(config["Login"]["MeetingLink"])


user_path = "/html/body/div/form[1]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/input[1]"
pass_path = "/html/body/div/form[1]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/input"
click(user_path)

#Automatically inpust the username and proceeds next
driver.find_element_by_xpath(user_path).send_keys(config["Login"]["Name"])
click("/html/body/div/form[1]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div/div[4]/div/div/div/div/input")
click('//*[@id="aadTile"]')
click('//*[@id="i0118"]')

#Automatically inpust the password and proceeds next
driver.find_element_by_xpath('//*[@id="i0118"]').send_keys(config["Login"]["Password"])

#Clicks next for the following pop-ups
click('//*[@id="idSIButton9"]')
click('//*[@id="idSIButton9"]')

#To make sure that the website is on the chat page
click('//*[@id="chatstab"]/div/div/chat-list-bridge/div/div[1]/div/ul/li/div[2]/div[1]/a')

# The while loop loops through the first page of classes (the active classes) and clicks on the desired class
i = 0
end = False
while end != True:
    i += 1
    element = driver.find_element_by_xpath(
        '''//*[@id="chatstab"]/div/div/chat-list-bridge/div/div[1]/div/ul/li/div[2]/div[%i]/a''' % i)
    if i % 29 == 0:
        click('''//*[@id="chatstab"]/div/div/chat-list-bridge/div/div[1]/div/ul/li/div[2]/div[%s]/a''' % (i))
    if element.get_attribute('title').lower() == c:
        click('''//*[@id="chatstab"]/div/div/chat-list-bridge/div/div[1]/div/ul/li/div[2]/div[%s]/a''' % (i))
        end = True

#Turns off the camera and microphone
click('''//*[@id="app-messages-header"]/ng-include/chat-header/div/div[3]/button[1]''')
click(
    '//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[2]/toggle-button[1]')
click('//*[@id="preJoinAudioButton"]')

# Clicks the join button
click(
    '''//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div/button''')

# Performs mouse move action onto the element
click('//*[@id="roster-button"]/ng-include')

end2 = False
remove = 'Currently in this meeting '
while not end2:
    time.sleep(5)
    p = driver.find_element_by_xpath('//*[@id="page-content-wrapper"]/div[1]/div/calling-screen/div/div[2]/meeting-panel-components/calling-roster/div/div[3]/div/div[1]/accordion/div/accordion-section[2]/div/calling-roster-section/div/div[1]/button').get_attribute('aria-label')
    p = p.replace(remove, '')
    if int(p) < 2:
        end2 = True
click('''//*[@id="hangup-button"]''')

