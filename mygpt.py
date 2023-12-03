import ssl

ssl._create_default_https_context = ssl._create_unverified_context

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
import time
from selenium.webdriver.common.by import By

# Using undetected_chromedriver to create an undetected ChromeDriver instance
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument(f"--user-data-dir=~/.config/google-chrome/Default")

driver = uc.Chrome(options=options)
# Load the website
driver.get("https://chat.openai.com/c/02cdfa5b-52f8-4ff4-a3cd-ae5af6af4381") 
# Find the element by ID and send keys
time.sleep(15)
def GPT(*args,**kwargs):
    new=""
    for i in args:
        new+=str(i)
    element = driver.find_element(By.ID,"prompt-textarea")
    element.send_keys(new)
    element.send_keys(Keys.ENTER)
    time.sleep(4)
    return driver.find_elements(By.CLASS_NAME,"markdown")[-1].text

