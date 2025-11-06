import configparser
config=configparser.RawConfigParser()
config.read("./Configaration/config.ini")

class Read_Config():
    @staticmethod
    def get_url():
        return config.get("Details","url")
    
    @staticmethod
    def get_username():
        return config.get("Details","username")
    
    @staticmethod
    def get_password():
        return config.get("Details","password")

