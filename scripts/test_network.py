import os
import sys
sys.path.append(os.getcwd())
from base.base_driver import init_driver
import time
from page.network_page import NetworkPage

class TestNetwork:

    def setup(self):
        self.driver = init_driver()
        self.network_page = NetworkPage(self.driver)

    def test_click_network_2G(self):
        self.network_page.click_mobile_network()
        self.network_page.click_first_network()
        self.network_page.click_change_network2G()

    def test_click_network_3G(self):
        self.network_page.click_mobile_network()
        self.network_page.click_first_network()
        self.network_page.click_change_network3G()