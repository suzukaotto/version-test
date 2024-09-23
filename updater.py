import requests
import re

git_version_doc = requests.get('https://github.com/suzukaotto/version-test/blob/master/VERSION').text

match = re.search(r'\[SWVERSION\](.*?)\[SWVERSIONEND\]', git_version_doc)

result = None
if match:
    result = match.group(1)

print(result)