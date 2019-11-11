from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class NetworkPage(BaseAction):

    more_button = By.XPATH, "//*[contains(@text,'更多')]"
    mobile_network_button = By.XPATH, "//*[contains(@text,'移动网络')]"
    first_network_button = By.XPATH, "//*[contains(@text,'首选网络类型')]"
    change_network2G_button = By.XPATH, "//*[contains(@text,'2G')]"
    change_network3G_button = By.XPATH, "//*[contains(@text,'3G')]"

    def __init__(self, driver):
        BaseAction.__init__(self, driver)
        self.click_more()

    def click_more(self):
        self.click(self.more_button)
        # self.find_element(self.more_button).click()
        # self.driver.find_element(By.XPATH, "//*[contains(@text,'更多')]").click()
        # self.driver.find_element_by_xpath("//*[contains(@text,'更多')]").click()

    def click_mobile_network(self):
        self.click(self.mobile_network_button)
        # self.find_element(self.mobile_network_button).click()
        # self.driver.find_element(By.XPATH, "//*[contains(@text,'移动网络')]").click()
        # self.driver.find_element_by_xpath("//*[contains(@text,'移动网络')]").click()

    def click_first_network(self):
        self.click(self.first_network_button)
        # self.find_element(self.first_network_button).click()
        # self.driver.find_element(By.XPATH, "//*[contains(@text,'首选网络类型')]").click()
        # self.driver.find_element_by_xpath("//*[contains(@text,'首选网络类型')]").click()

    def click_change_network2G(self):
        self.click(self.change_network2G_button)
        # self.find_element(self.change_network2G_button).click()
        # self.driver.find_element(By.XPATH, "//*[contains(@text,'2G')]").click()
        # self.driver.find_element_by_xpath("//*[contains(@text,'2G')]").click()

    def click_change_network3G(self):
        self.click(self.change_network3G_button)
        # self.find_element(self.change_network3G_button).click()
        # self.driver.find_element(By.XPATH, "//*[contains(@text,'3G')]").click()
        # self.driver.find_element_by_xpath("//*[contains(@text,'3G')]").click()
