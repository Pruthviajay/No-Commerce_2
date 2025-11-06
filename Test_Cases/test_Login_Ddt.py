from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.edge.webdriver import WebDriver
from PageObject.Login_Page import Login_Page
from Test_Cases.conftest import setup
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities.Config_reader import Read_Config
from Utilities import Excel_Utils
import time



class Test_01_Login_Ddt():

    url=Read_Config.get_url()
    path="./Test_Data/Data.xlsx"
    Row_Count=Excel_Utils.Row_Count(path,"Sheet1")
    Test_Result=[]


    def test_login(self,setup: WebDriver | WebDriver):
        self.driver=setup
        self.driver.get(self.url)
        Login=Login_Page(self.driver)

        for r in range(2,self.Row_Count+1):
            self.username=Excel_Utils.Read_Excel(self.path,"Sheet1",r,1)
            self.password=Excel_Utils.Read_Excel(self.path,"Sheet1",r,2)
            self.exp=Excel_Utils.Read_Excel(self.path,"Sheet1",r,3)
            Login.login()
            time.sleep(3)


            act_title=self.driver.title
            Expected_Title="Dashboard / nopCommerce administration"
            if act_title==Expected_Title:
                if self.exp == "Pass":
                    print("Test is passed")
                    self.Test_Result.append("Pass")
                elif self.exp == "Fail":
                    print("Test is Failed")
                    self.Test_Result.append("Fail")

            elif act_title != Expected_Title:
                if self.exp=="Fail":
                    print("Test is passed")
                    self.Test_Result.append("Pass")

                elif self.exp=="Pass":
                    print("Test is Failed")
                    self.Test_Result.append("Fail")
            if "Fail" not in self.Test_Result:
                print("Test is passed")
                assert True
            else:
                print("TEst is failed")
                assert False
            self.driver.quit()

                                                    

        


