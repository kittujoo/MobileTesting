from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

    def do_send_keys(self, locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def swipe(self, start_x, start_y, end_x, end_y, time_leap_in_ms):
        self.driver.swipe(start_x, start_y, end_x, end_y, time_leap_in_ms)

    def get_price(self, locator):
        return str(self.driver.find_element(*locator).text).replace(' ', '')
