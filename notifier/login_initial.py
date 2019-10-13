from selenium import webdriver
from selenium.webdriver.common.by import By
import contextlib
from selenium.webdriver import Remote
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.chrome.options import Options

class Cisco:
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--no-sandbox')
    driver = webdriver.Chrome('/home/jaymoh/Desktop/Projects/webscrapping/ciscoselenium/chromedriver_linux64/chromedriver')

    email = 'lelerukjaymoh@gmail.com'
    password = 'jay17kish05'
    url = 'https://www.netacad.com/portal/saml_login'  

    def login(self):
        email = self.email
        self.driver.get(self.url)
        self.driver.find_element_by_class_name('input--dirty').send_keys(email)
        self.driver.find_element_by_class_name('btn--primary').click()
        old_page_button = self.driver.find_element_by_class_name('btn').get_attribute('value')
        print(old_page_button)
        
        self.driver.close()
        quit()

    # login(self)

        # self.driver.find_element_by_id('password').send_keys(password)
        # self.driver.find_element_by_id('kc-login').click()





# class MyRemote(Remote):
#     @contextlib.contextmanager
#     def wait_for_page_load(self, timeout=30):
#         old_page = self.find_element_by_tag_name('html')
#         yield
#         WebDriverWait(self, timeout).until(staleness_of(old_page))