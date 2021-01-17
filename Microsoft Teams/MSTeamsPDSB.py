import time
import keyboard
import schedule
import configparser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# The click function clicks the desired path
def manipulateLink(s):
    newLink = s.replace('%', '%%')
    return newLink


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


def joinClass():
    global driver
    # The path to the location where the chromedriver is located at
    PATH = "chromedriver.exe"

    # Automatically adds the profile 1 user to chrome to prevent any future sign ins after the first time
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.media_stream_mic": 1,
        "profile.default_content_setting_values.media_stream_camera": 1,
    })
    options.add_argument('--lang=en-US')
    driver = webdriver.Chrome(executable_path=PATH, options=options)

    # Parse ini file
    config = configparser.ConfigParser()
    config.read("config.ini")
    driver.get(
        'https://teams.microsoft.com/_#/conversations/19:meeting_Nzc3NWFjOTctNTQxMC00NWI0LTk0YWMtZmE1Y2VlMzVlYjhm@thread.v2?ctx=chat')
    # The driver obtains the path to the website (Microsoft Teams)
    # Wait for the website to load in

    user_path = '//*[@id="i0116"]'
    pass_path = '//*[@id="i0118"]'
    click(user_path)
    driver.find_element_by_xpath(user_path).send_keys(config["Login"]["Name"])
    click("/html/body/div/form[1]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div/div[4]/div/div/div/div/input")

    click('//*[@id="aadTile"]')
    click(pass_path)
    driver.find_element_by_xpath(pass_path).send_keys(config["Login"]["Password"])
    click('//*[@id="idSIButton9"]')
    click('//*[@id="idSIButton9"]')

    driver.get(config.get('Login', 'MeetingLink', raw=True))
    keyboard.send('enter')
    click('//*[@id="buttonsbox"]/button[2]')
    click(
        '//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[2]/toggle-button[1]')
    click('//*[@id="preJoinAudioButton"]')

    # Clicks the join button
    click(
        '''//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div/button''')

    # Performs mouse move action onto the element
    click('//*[@id="roster-button"]/ng-include')
    click('//*[@id="callingButtons-showMoreBtn"]/ng-include')

    end2 = False
    remove = 'Currently in this meeting '
    while not end2:
        time.sleep(5)
        p = driver.find_element_by_xpath(
            '//*[@id="page-content-wrapper"]/div[1]/div/calling-screen/div/div[2]/meeting-panel-components/calling-roster/div/div[3]/div/div[1]/accordion/div/accordion-section[2]/div/calling-roster-section/div/div[1]/button').get_attribute(
            'aria-label')
        p = p.replace(remove, '')
        if int(p) < 2:
            end2 = True
    click('''//*[@id="hangup-button"]''')

schedule.every().day.at('23:46').do(joinClass)

while True:
    schedule.run_pending()
    time.sleep(5)