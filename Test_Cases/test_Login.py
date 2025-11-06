from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from PageObject.Login_Page import Login_Page
from Test_Cases.conftest import setup
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities.Config_reader import Read_Config




class Test_01_Login():

    url=Read_Config.get_url()
    username=Read_Config.get_username()
    password=Read_Config.get_password()

    def test_homepage_title(self,setup):
        self.driver=setup
        self.driver.get(self.url)
        actual_title=self.driver.title
        print(self.driver.title)
        if actual_title=="nopCommerce demo store. Login":
            assert True 
        else:
            assert False

        self.driver.quit()

    def test_login(self,setup):
        self.driver=setup
        self.driver.get(self.url)

        Login=Login_Page(self.driver)
        # wait=WebDriverWait(self.driver,10,poll_frequency=2,ignored_exceptions=[Exception])
        # wait.until(EC.presence_of_element_located((Login.text_Box_User_Name)))
                                                     
        Login.set_username(self.username)

        Login.set_password(self.password)
        
        Login.login()
        actual_title=self.driver.title
        if actual_title=="Dashboard / nopCommerce administration":
            assert True  
        else :
            self.driver.save_screenshot("./Screenshots.test_login.png")
            assert False
        self.driver.quit()
                                                                        

        


