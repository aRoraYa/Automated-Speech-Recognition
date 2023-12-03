from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--use-fake-ui-for-media-stream")
# chrome_options.add_argument("--use-fake-ui-for-media-stream")  # Use fake UI to automatically grant permission
# chrome_options.add_argument("--use-fake-device-for-media-stream")

# chrome_options.add_argument('--headless')
# chrome_options.headless = True
driver = webdriver.Chrome(options=chrome_options)
driver.minimize_window()
website = r"file:///Users/asifali/Desktop/jarvis/voice.html"

driver.get(website)


def command():
    print("LISTENING ... ")
    driver.find_element(by=By.ID, value='start').click()
    while 1:
        if driver.find_element(by=By.ID, value='output').text != "":
            print("you said : " + driver.find_element(by=By.ID, value='output').text)
            a = driver.find_element(by=By.ID, value='output').text
            driver.find_element(by=By.ID, value='end').click()
            return a

