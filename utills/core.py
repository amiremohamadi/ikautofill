from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from model.person import Person
from config import config

class Core:
    __slots__ = (
        'driver',
    )

    def __init__(self):
        self.driver = webdriver.Chrome(
            config['webdriver']
        )

    def fill(self, _person):
        self.driver.get(config['url'])

        # wait for element until load
        try:
            element_present = EC.presence_of_element_located((By.NAME, 'firstName'))
            WebDriverWait(self.driver, 20).until(element_present)
        # in case of bad internet connection or other cases that element
        # not loaded, print the error message
        except TimeoutException:
            print('timed out waiting for page to load')
            exit(-1)
                
        first_name = self.driver.find_element_by_name('firstName')
        first_name.send_keys(_person.first_name)

        last_name = self.driver.find_element_by_name('lastName')
        last_name.send_keys(_person.last_name)
        
        user_name = self.driver.find_element_by_name('userName')
        user_name.send_keys(_person.national_id)
        
        password = self.driver.find_element_by_name('password')
        password.send_keys(_person.birth_certificate)

        phone_number = self.driver.find_element_by_name('cellPhoneNo')
        phone_number.send_keys(_person.phone)
        
        provinces = Select(self.driver.find_element_by_id('directiveProvince'))
        provinces.select_by_visible_text(_person.state)

        city = Select(self.driver.find_element_by_id('directiveCity'))
        city.select_by_visible_text(_person.city)

        date_picker = self.driver.find_element_by_id('bd-main-birthDate')
        # show date picker -> it enables selenium to select a date
        self.driver.execute_script("arguments[0].setAttribute('class','bd-main')", date_picker)

        # trick: indexes are start from 0, so it'll be okay to add -1 to birth_month
        date_month = Select(self.driver.find_element_by_id('bd-month-birthDate'))
        date_month.select_by_index(_person.birth_month - 1)

        date_year = Select(self.driver.find_element_by_class_name('bd-year'))
        date_year.select_by_index(_person.birth_year - 1303)

        date_day = self.driver.find_element_by_class_name('day-' + str(_person.birth_day))
        date_day.click()        
