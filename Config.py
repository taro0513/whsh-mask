import configparser
import sys
import os

class config():
    def __init__(self, ini_name='setfile.ini',section=None):
        self.local = sys.path[0]
        self.config = configparser.ConfigParser()
        self.ini_name = os.path.join(self.local,ini_name) if ini_name == 'setfile.ini' else ini_name
        try:
            self.config.read(self.ini_name)
            self.section = section
        except Exception as e: print(e)
    def data(self, section=None, key=None):
        if section :
            try:
                if key: return self.config[section][key]
                else: return self.config[section]
            except Exception as e: print(e)
        else: 
            try: 
                if key: return self.config[self.section][key]
                else: return self.config[self.section]
            except: return self.config.sections()
    def edit(self, key, value, ini_name='setfile.ini', section=None):
        section = self.section if section == None else section
        self.config[section][key] = value
        with open(ini_name, 'w') as configfile:
            self.config.write(configfile)