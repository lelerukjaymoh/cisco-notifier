from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options  
import time


class See:
    def me(self):
        url = 'file:///home/jaymoh/Desktop/Projects/webscrapping/ciscoselenium/Course%20Modules_%20scan_cs_sep2019.html'
        driver = webdriver.Chrome('/home/jaymoh/Desktop/Projects/webscrapping/ciscoselenium/chromedriver_linux64/chromedriver')

        driver.get(url)
        for each in driver.find_elements_by_css_selector('a.ig-title'):
            if each.text.endswith('Exam'):
                module_link = each.get_attribute('href')
                print(module_link)

                # Testing with module 7 which is not activated
                driver.get('https://1277436.netacad.com/courses/894061/modules/items/60536852')
                try:
                    for each in driver.find_elements_by_css_selector('div.alert-message'):
                        print(each.text)
                except:
                    print('Alert not found')
                else:
                    print("Will try something else")

        return driver