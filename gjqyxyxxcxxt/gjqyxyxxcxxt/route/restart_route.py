# -*- coding: utf-8 -*-
import time
from selenium import webdriver

class RouteRestart(object):
    def __init__(self):
        url = 'http://192.168.3.1/html/home.html'
        self.browser = webdriver.PhantomJS()
        self.browser.get(url)

    def run(self):
        search_el = self.browser.find_element_by_id('logout_span')
        search_el.click()
        time.sleep(0.5)
        input_el = self.browser.find_element_by_id('username')
        input_el.clear()
        input_el.send_keys('admin')  
        input_el = self.browser.find_element_by_id('password')
        input_el.clear()
        input_el.send_keys('admin') 
        input_el = self.browser.find_element_by_id('pop_login')
        input_el.click()   
        time.sleep(1)
        input_el = self.browser.find_element_by_id('settings')
        input_el.click()  
        time.sleep(0.5)
        input_el = self.browser.find_element_by_id('system')
        input_el.click()   
        input_el = self.browser.find_element_by_id('label_reboot')
        input_el.click()
        time.sleep(2)
        self.browser.save_screenshot('screenshot.png')
        input_el = self.browser.find_element_by_id('reboot_apply_button')
        input_el.click() 
        input_el = self.browser.find_element_by_id('pop_confirm')
        input_el.click() 
        time.sleep(1)

    def crack(self):
        """执行破解程序

        """
        raise NotImplementedError

if __name__ == '__main__':
    restart = RouteRestart()
    restart.run()
