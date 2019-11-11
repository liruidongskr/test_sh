from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class DisplayPage(BaseAction):

    # 显示按钮
    display_button = By.XPATH, "//*[contains(@text,'显示')]"
    search_button = By.ID, "com.android.settings:id/search"
    search_text = By.ID, "android:id/search_src_text"
    back_button = By.CLASS_NAME, "android.widget.ImageButton"

    def __init__(self, driver):
        BaseAction.__init__(self, driver)
        self.click_display()

    def click_display(self):
        self.click(self.display_button)
        # self.find_element(self.display_button).click()
        # self.driver.find_element(self.display_button).click()
        # self.driver.find_element_by_xpath("//*[contains(@text,'显示')]").click()

    def click_search(self):
        self.click(self.search_button)
        # self.find_element(self.search_button).click()
        # self.driver.find_element(self.search_button).click()
        # self.driver.find_element_by_id("com.android.settings:id/search").click()

    def send_keys_input(self, value):
        self.input_send_keys(self.search_text, value)
        # self.driver.find_element(self.search_text).send_keys(value)
        # self.driver.find_element_by_id("android:id/search_src_text").send_keys(value)

    def click_back(self):
        self.click(self.back_button)
        # self.find_element(self.back_button).click()
        # self.driver.find_element(self.back_button).click()
        # self.driver.find_element_by_class_name("android.widget.ImageButton").click()

    # def find_element(self, loc):
    #     return self.driver.find_element(loc[0], loc[1])