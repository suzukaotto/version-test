import requests
import re

class Updater:
    def __init__(self):
        self.api_timeout = 5
        self.check_url = None
        
    def set_check_url(self, url):
        self.check_url = url
        
    def get_now_version(self):
        if self.check_url is None:
            return None
        
        try:
            git_version_doc = requests.get(self.check_url, timeout=self.api_timeout).text
        except:
            return None
        
        return self.find_version(git_version_doc)
    
    def find_version(self, str, pattern=r'\[SWVERSION\](.*?)\[SWVERSIONEND\]'):
        match = re.search(pattern, str)
        
        result = None
        if match:
            result = match.group(1)
        
        result = float(result)
        
        return result