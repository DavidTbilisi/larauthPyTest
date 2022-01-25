# from datetime import datetime
import time
import subprocess
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from configs import *
import logging

logging.basicConfig(
    filename='test.log',
    encoding='utf-8',
    filemode='w',
    format='[%(asctime)s] %(levelname)s: %(message)s',
    level=logging.INFO)


def migrate_and_seed():
    subprocess.run(["/usr/bin/php", f"{root_dir}artisan", "migrate:fresh", "--seed"])


# subprocess.run(["/usr/bin/php",f"{root_dir}artisan","serve","&"])

if migration_start == "yes":
    migrate_and_seed()

driver = webdriver.Firefox()
driver.maximize_window()


def go_uri(uri):
    driver.get(website + uri)


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
        {"selector": "[name=name]", "value": "სატესტო თეიბლი", },
        {"selector": "[name=tablename]", "value": "testtable", },
        {"selector": "[name*=names]", "value": "ველი1", },
        {"selector": "[name*=field]", "value": "testfield", },
    ]

    for f in data:
        elem = driver.find_element_by_css_selector(f.get('selector'))
        elem.clear()
        elem.send_keys(f.get('value'))

    time.sleep(wait)
    elem = driver.find_element_by_css_selector("[type=submit]")
    elem.send_keys(Keys.ENTER)


def edit_type(tablename='testtable'):
    go_uri(f"/admin/types/show/{tablename}")
    time.sleep(wait)

    # add field
    elem = driver.find_element_by_css_selector(".add-button span")
    elem.click()
    time.sleep(wait)

    # edit field name
    elem = driver.find_element_by_css_selector("#newColumn")
    elem.send_keys("thenewcolumn")
    submit_btn = driver.find_element_by_css_selector("button.btn.btn-success")
    submit_btn.click()

    # edit translation
    elem = driver.find_element_by_css_selector("#thenewcolumn")
    elem.clear()
    elem.send_keys("ველი2", Keys.TAB)
    time.sleep(wait)

    # save changes
    submit_btn = driver.find_element_by_css_selector("button.btn.btn-success")
    submit_btn.click()


def delete_type():
    go_uri("/admin/types")
    submit_btn = driver.find_element_by_css_selector("button.btn.btn-danger")
    submit_btn.click()


login(user, password)
time.sleep(wait)

add_type()
time.sleep(wait)

edit_type()
time.sleep(wait)

try:
    delete_type()
    time.sleep(wait)
except:
    print("you have some problem")

driver.close()

if migration_end == "yes":
    migrate_and_seed()
