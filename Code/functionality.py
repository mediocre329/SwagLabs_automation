from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import Code.constants as const
from prettytable import PrettyTable





class Swaglab (webdriver.Chrome):

    def __init__(self, teardown = False):
        self.teardown = teardown
        super(Swaglab,self).__init__()
        self.implicitly_wait(10)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()


    def land_first_page(self):

        self.get(const.BASE_URL)

    def login(self):
        username = self.find_element(By.ID, 'user-name')
        username.send_keys('standard_user')

        password = self.find_element(By.ID, 'password')
        password.send_keys('secret_sauce')

        submit_login =self.find_element(By.ID, 'login-button')
        submit_login.click()

    def filter(self):
        price_filter = self.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select/option[3]')
        price_filter.click()

    def get_item(self):
        items = self.find_elements(By.CLASS_NAME, 'inventory_item')

        for item in items :
            product = item.find_element(By.CLASS_NAME, 'inventory_item_name')
            price = item.find_element(By.CLASS_NAME, 'inventory_item_price')

            table = PrettyTable(
                field_names=["product","price"]
            )
            table.add_row([product.text,price.text])
            print(table)