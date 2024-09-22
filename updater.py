import requests

rst = requests.get('https://raw.githubusercontent.com/suzukaotto/version-test/refs/heads/master/VERSION')
print(rst.text)