
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


def edit_type(tablename='testtable'):
    go_uri(f"/admin/types/show/{tablename}")
    time.sleep(2)
    
    # add field
    elem = driver.find_element_by_css_selector(".add-button span")
    elem.click()
    time.sleep(2)
    
    # edit field name
    elem = driver.find_element_by_css_selector("#newColumn")
    elem.send_keys("thenewcolumn")
    submit_btn = driver.find_element_by_css_selector("button.btn.btn-success")
    submit_btn.click()
    
    # edit translation
    elem = driver.find_element_by_css_selector("#thenewcolumn")
    elem.clear()
    elem.send_keys("ველი2", Keys.TAB)
    time.sleep(2)

    # save changes
    submit_btn = driver.find_element_by_css_selector("button.btn.btn-success")
    submit_btn.click()