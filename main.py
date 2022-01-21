# from datetime import datetime
import time
import subprocess
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from configs import *

subprocess.run(["/usr/bin/php",f"{root_dir}artisan","migrate:fresh","--seed"])
# subprocess.run(["/usr/bin/php",f"{root_dir}artisan","serve","&"])

driver = webdriver.Firefox()
driver.maximize_window()


def go_uri(uri):
    driver.get(website+uri)

def login(email, password):
    
    go_uri("/login")

    elem = driver.find_element_by_css_selector("#email")
    elem.clear()
    elem.send_keys(email)
    # elem.send_keys(Keys.RETURN)

    elem = driver.find_element_by_css_selector("#password")
    elem.clear()
    elem.send_keys(password)
    elem = driver.find_element_by_css_selector("button[type=submit]")
    elem.send_keys(Keys.RETURN)


def add_type():
    go_uri("/admin/types/add")
    data = [
        {"selector": "[name=name]","value": "სატესტო თეიბლი",},
        {"selector": "[name=tablename]","value": "testtable",},
        {"selector": "[name*=names]","value": "ველი1",},
        {"selector": "[name*=field]","value": "testfield",},
        ]

    for f in data:
        elem = driver.find_element_by_css_selector(f.get('selector'))
        elem.clear()
        elem.send_keys(f.get('value'))

    time.sleep(2)
    elem = driver.find_element_by_css_selector("[type=submit]")
    elem.send_keys(Keys.ENTER)




login(user, password)
time.sleep(5)
add_type()
time.sleep(5)

# driver.close()
