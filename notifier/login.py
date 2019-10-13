from django.conf import settings
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options  
import time

class Scraper:
    chrome_options = Options()  
    Options.headless = True   

    driver = webdriver.Chrome('/home/jaymoh/Desktop/Projects/webscrapping/ciscoselenium/chromedriver_linux64/chromedriver', chrome_options=chrome_options)

    
    def login(self):
        driver = self.driver
        username = settings.USERNAME
        password = settings.PASS
        url = 'https://www.netacad.com/portal/saml_login'  

        driver.get(url)
        driver.find_element_by_class_name('input--dirty').send_keys(username)
        driver.find_element_by_class_name('btn--primary').click()

        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'password')))   
        driver.find_element_by_id('password').send_keys(password)
        driver.find_element_by_css_selector('div.col-xs-12 button').send_keys(Keys.ENTER)

        return driver 

    def courses_status(self, driver):
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'dot')))
        for each in driver.find_elements_by_class_name('status-in-progress'):
            course_link = each.find_element_by_css_selector('div.course-launcher a').get_attribute('href')
            print(course_link+"/modules")
            driver.get(course_link+"/modules")
            WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, 'span.ellipsible')))
            for each in driver.find_elements_by_css_selector('span.ellipsible'):
                print(each.text)


            # for each in driver.find_element_by_css_selector('a.ig-title').get_attribute('href'):
            #     print(each)

        driver.quit()