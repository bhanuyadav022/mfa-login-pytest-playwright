import os
import json

class ConfigManager:
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    CONFIG_PATH = os.path.join(ROOT_DIR, '../config.json') 
    
    #read_config
    @staticmethod
    def read_config ():
        with open(ConfigManager.CONFIG_PATH, 'r') as file:
            config_data = json.load(file)
        return config_data
