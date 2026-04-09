import os
import configparser #library to read config from a config.ini file

config = configparser.RawConfigParser()

config_path = "configs/config.ini"
config_path_from_course =  os.path.abspath(os.getcwd()) + "//configs//config.ini" #os.getcwd = get current working directory (if this file is run directly then it is "utils")
print(config_path_from_course)
config.read(config_path)
print("Read config")

class ReadConfig:
    @staticmethod
    def get_property(key):
        return config.get("commonInfo", key)
