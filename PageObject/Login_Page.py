from selenium.webdriver.common.by import By

class Login_Page():
    text_Box_User_Name="Email"
    text_Box_Password="Password"
    btn_Login_Xpath="//button[normalize-space()='Log in']"
    btn_Logout_Xpath="//a[contains(text(),'Logout')]"

    def __init__(self,driver):
        self.driver=driver 
        
    def set_username(self,username):
        self.driver.find_element(By.ID,self.text_Box_User_Name).clear()
        self.driver.find_element(By.ID,self.text_Box_User_Name).send_keys(username)
    
    def set_password(self,password):
        self.driver.find_element(By.ID,self.text_Box_Password).clear()
        self.driver.find_element(By.ID,self.text_Box_Password).send_keys(password)
    
    def login(self):
        self.driver.find_element(By.XPATH,self.btn_Login_Xpath).click()

    def logout(self):
        self.driver.find_element(By.XPATH,self.btn_Logout_Xpath).click()