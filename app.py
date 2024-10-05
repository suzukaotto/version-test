import requests
from updater import Updater

AppUpdater = Updater()
AppUpdater.set_check_url("https://github.com/suzukaotto/version-test/blob/master/VERSION")
CLOUD_VERSION = AppUpdater.get_now_version()

with open("./VERSION", "r") as f:
    VERSION = AppUpdater.find_version(f.read().strip())

print(f"Hello, now version is {VERSION}, cloud version is {CLOUD_VERSION}")

if VERSION < CLOUD_VERSION:
    print("Update available!")
else:
    print("Your lasted version!")
