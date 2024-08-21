from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get('https://en.wikipedia.org/wiki/Document_Object_Model')
browser.save_screenshot('Dom.png')
time.sleep(10)
browser.get('https://ru.wikipedia.org/wiki/Selenium')
browser.save_screenshot('Selenium.png')
time.sleep(3)
browser.refresh()