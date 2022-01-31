# from datetime import datetime
import time
import subprocess
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
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
    elem = driver.find_elements_by_css_selector("button.btn.btn-danger")[1]
    elem.click()
    alert = driver.switch_to.alert
    print(alert.text)
    alert.accept()


def helper_add_io(prefix="pre", identifier='154', suffix="suf", fond="Fond name"):
    pref = driver.find_element_by_css_selector("#prefix")
    ident = driver.find_element_by_css_selector("#identifier")
    suf = driver.find_element_by_css_selector("#suffix")
    type = driver.find_element_by_css_selector("#type")

    pref.clear()
    pref.send_keys(prefix, Keys.TAB)

    ident.clear()
    ident.send_keys(identifier, Keys.TAB)

    suf.clear()
    suf.send_keys(suffix, Keys.TAB)

    select_type = Select(type)
    select_type.select_by_value("fonds")  # select fond
    time.sleep(wait)

    fond_name = driver.find_element_by_css_selector("#name")
    fond_name.send_keys(fond)



def add_io():
    go_uri("/admin/io")
    elem = driver.find_element_by_css_selector(".add-button span")
    elem.click()
    time.sleep(wait)

    helper_add_io("1", 1, '1', 'fond1')

    # save changes
    submit_btn = driver.find_element_by_css_selector("button.btn.btn-success")
    submit_btn.click()


def add_io_child():
    go_uri("/admin/io/show/1")
    elem = driver.find_element_by_css_selector(".add-button span")
    elem.click()
    time.sleep(wait)

    helper_add_io("2", 2, '2', 'fond2')

    # save changes
    submit_btn = driver.find_element_by_css_selector("button.btn.btn-success")
    submit_btn.click()

def edit_io(prefix="p", identifier=1, suffix="s"):
    go_uri("/admin/io")
    elem = driver.find_elements_by_css_selector(".btn.btn-info")[0]
    elem.click()

    pref = driver.find_element_by_css_selector("#prefix")
    ident = driver.find_element_by_css_selector("#identifier")
    suf = driver.find_element_by_css_selector("#suffix")

    pref.clear()
    pref.send_keys(prefix, Keys.TAB)

    ident.clear()
    ident.send_keys(identifier, Keys.TAB)

    suf.clear()
    suf.send_keys(suffix, Keys.TAB)

    # save changes
    submit_btn = driver.find_element_by_css_selector("button.btn.btn-success")
    submit_btn.click()

def edit_io_child(prefix="c", identifier=1, suffix="c"):
    go_uri("/admin/io")
    elem = driver.find_elements_by_css_selector(".btn.btn-info")[1]
    elem.click()

    pref = driver.find_element_by_css_selector("#prefix")
    ident = driver.find_element_by_css_selector("#identifier")
    suf = driver.find_element_by_css_selector("#suffix")

    pref.clear()
    pref.send_keys(prefix, Keys.TAB)

    ident.clear()
    ident.send_keys(identifier, Keys.TAB)

    suf.clear()
    suf.send_keys(suffix, Keys.TAB)

    # save changes
    submit_btn = driver.find_element_by_css_selector("button.btn.btn-success")
    submit_btn.click()


def delete_io_child():
    go_uri("/admin/io")
    elem = driver.find_elements_by_css_selector(".btn.btn-danger")[1]
    elem.click()

    alert = driver.switch_to.alert
    print(alert.text)
    time.sleep(1)
    alert.accept()


def delete_io():
    go_uri("/admin/io")
    elem = driver.find_elements_by_css_selector(".btn.btn-danger")[0]
    elem.click()

    alert = driver.switch_to.alert
    print(alert.text)
    time.sleep(1)
    alert.accept()

################
## types test ##
################


login(user, password)
time.sleep(wait)


def types_test():
    add_type()
    time.sleep(wait)

    edit_type()
    time.sleep(wait)

    delete_type()
    time.sleep(wait)


###################

def io_test():
    add_io()
    time.sleep(wait)

    add_io_child()
    time.sleep(wait)

    edit_io()
    time.sleep(wait)

    edit_io_child()
    time.sleep(wait)

    delete_io_child()
    time.sleep(wait)

    delete_io()
    time.sleep(wait)


types_test()
io_test()


try:
    print("done")
except:
    print("you have some problem")

driver.close()

if migration_end == "yes":
    migrate_and_seed()
