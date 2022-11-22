import document as document
import timer as timer
from selenium import webdriver
from behave import *
from pytest_bdd import scenario, given, when, then
from ssl import DER_cert_to_PEM_cert
import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

driver: WebDriver = webdriver.Chrome("C:\Chromewebdrivers\\chromedriver.exe")

driver.get("http://localhost:4200")

@given(u': I Launched the Chrome Web Browser And Login the Portal')


def loginportal():
    driver.find_element(By.NAME, "username").send_keys("admin@shopizer.com")
    driver.find_element(By.NAME, "password").send_keys("password")
    ele = driver.find_element(By.CLASS_NAME, "container-login100-form-btn")
    ele.click()

loginportal()

time.sleep(2)

# Creating Store

driver.get("http://localhost:4200/#/pages/store-management/create-store")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "#name").send_keys("zstore")
driver.find_element(By.CSS_SELECTOR, "#code").send_keys("zstore123")
driver.find_element(By.CSS_SELECTOR, "#phone").send_keys("04231234123")
driver.find_element(By.CSS_SELECTOR, "#email").send_keys("ziaulhaq@gmail.com")
driver.find_element(By.CSS_SELECTOR, "#address").send_keys("Mughlpura")
driver.find_element(By.CSS_SELECTOR, "#phone").send_keys("03312341234")
driver.find_element(By.CSS_SELECTOR, "#city").send_keys("Lahore")
driver.find_element(By.CSS_SELECTOR, "#postalCode").send_keys("5ss180")
driver.find_element(By.XPATH, "/html[1]/body[1]/ngx-app[1]/div[1]/ngx-pages[1]/ngx-sample-layout[1]/nb-layout[1]/div[1]/div[1]/div[1]/div[1]/div[1]/nb-layout-column[1]/ngx-store-management[1]/div[1]/div[1]/ngx-store-creation[1]/div[1]/ngx-store-form[1]/div[1]/form[1]/nb-card[1]/nb-card-body[1]/div[6]/div[1]/nb-checkbox[2]/label[1]/span[1]").click()
time.sleep(2)


element = driver.find_element(By.XPATH, "/html[1]/body[1]/ngx-app[1]/div[1]/ngx-pages[1]/ngx-sample-layout[1]/nb-layout[1]/div[1]/div[1]/div[1]/div[1]/div[1]/nb-layout-column[1]/ngx-store-management[1]/div[1]/div[1]/ngx-store-creation[1]/div[1]/ngx-store-form[1]/div[1]/nb-card-header[1]/div[2]/button[1]")

time.sleep(2)
driver.execute_script("arguments[0].click();", element)

time.sleep(5)



# Creating another store

driver.get("http://localhost:4200/#/pages/store-management/create-store")

time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "#name").send_keys("zstore1")
driver.find_element(By.CSS_SELECTOR, "#code").send_keys("zstore1123")
driver.find_element(By.CSS_SELECTOR, "#phone").send_keys("04231231231")
driver.find_element(By.CSS_SELECTOR, "#email").send_keys("ziaulhaq1@gmail.com")
driver.find_element(By.CSS_SELECTOR, "#address").send_keys("Tajbagh")
driver.find_element(By.CSS_SELECTOR, "#phone").send_keys("03312345123")
driver.find_element(By.CSS_SELECTOR, "#city").send_keys("Lahore")
driver.find_element(By.CSS_SELECTOR, "#postalCode").send_keys("5ss182")
driver.find_element(By.XPATH, "/html[1]/body[1]/ngx-app[1]/div[1]/ngx-pages[1]/ngx-sample-layout[1]/nb-layout[1]/div[1]/div[1]/div[1]/div[1]/div[1]/nb-layout-column[1]/ngx-store-management[1]/div[1]/div[1]/ngx-store-creation[1]/div[1]/ngx-store-form[1]/div[1]/form[1]/nb-card[1]/nb-card-body[1]/div[6]/div[1]/nb-checkbox[2]/label[1]/span[1]").click()
time.sleep(2)


element = driver.find_element(By.XPATH, "/html[1]/body[1]/ngx-app[1]/div[1]/ngx-pages[1]/ngx-sample-layout[1]/nb-layout[1]/div[1]/div[1]/div[1]/div[1]/div[1]/nb-layout-column[1]/ngx-store-management[1]/div[1]/div[1]/ngx-store-creation[1]/div[1]/ngx-store-form[1]/div[1]/nb-card-header[1]/div[2]/button[1]")

time.sleep(2)
driver.execute_script("arguments[0].click();", element)

time.sleep(5)





# Creating another store
driver.get("http://localhost:4200/#/pages/store-management/create-store")

time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "#name").send_keys("zstore2")
driver.find_element(By.CSS_SELECTOR, "#code").send_keys("zstore2123")
driver.find_element(By.CSS_SELECTOR, "#phone").send_keys("0423121212")
driver.find_element(By.CSS_SELECTOR, "#email").send_keys("ziaulhaq2@gmail.com")
driver.find_element(By.CSS_SELECTOR, "#address").send_keys("Askari 11")
driver.find_element(By.CSS_SELECTOR, "#phone").send_keys("03312121212")
driver.find_element(By.CSS_SELECTOR, "#city").send_keys("Lahore")
driver.find_element(By.CSS_SELECTOR, "#postalCode").send_keys("5ss183")
driver.find_element(By.XPATH, "/html[1]/body[1]/ngx-app[1]/div[1]/ngx-pages[1]/ngx-sample-layout[1]/nb-layout[1]/div[1]/div[1]/div[1]/div[1]/div[1]/nb-layout-column[1]/ngx-store-management[1]/div[1]/div[1]/ngx-store-creation[1]/div[1]/ngx-store-form[1]/div[1]/form[1]/nb-card[1]/nb-card-body[1]/div[6]/div[1]/nb-checkbox[2]/label[1]/span[1]").click()
time.sleep(2)


element = driver.find_element(By.XPATH, "/html[1]/body[1]/ngx-app[1]/div[1]/ngx-pages[1]/ngx-sample-layout[1]/nb-layout[1]/div[1]/div[1]/div[1]/div[1]/div[1]/nb-layout-column[1]/ngx-store-management[1]/div[1]/div[1]/ngx-store-creation[1]/div[1]/ngx-store-form[1]/div[1]/nb-card-header[1]/div[2]/button[1]")

time.sleep(2)
driver.execute_script("arguments[0].click();", element)

time.sleep(5)






# Searching a store with correct store name

@When(u'Admin search a store with correct store name')

def Search_with_correct_name():
    driver.find_element(By.XPATH, "/html/body/ngx-app/div/ngx-pages/ngx-sample-layout/nb-layout/div/div/div/div/div/nb-layout-column/ngx-store-management/div/div/ngx-stores-list/nb-card/nb-card-body/div/ng2-smart-table/table/thead/tr[2]/th[4]/ng2-smart-table-filter/div/default-table-filter/input-filter/input").send_keys("zstore")
    time.sleep(2)


    driver.find_element(By.XPATH, "/html/body/ngx-app/div/ngx-pages/ngx-sample-layout/nb-layout/div/div/div/div/div/nb-layout-column/ngx-store-management/div/div/ngx-stores-list/nb-card/nb-card-body/div/ng2-smart-table/table/thead/tr[2]/th[4]/ng2-smart-table-filter/div/default-table-filter/input-filter/input").clear()
    time.sleep(2)

Search_with_correct_name()


# Searching a store with wrong store name

@When(u'Admin search a store with wrong store name')

def Search_with_wrong_name():
    driver.find_element(By.XPATH, "/html/body/ngx-app/div/ngx-pages/ngx-sample-layout/nb-layout/div/div/div/div/div/nb-layout-column/ngx-store-management/div/div/ngx-stores-list/nb-card/nb-card-body/div/ng2-smart-table/table/thead/tr[2]/th[4]/ng2-smart-table-filter/div/default-table-filter/input-filter/input").send_keys("zstore12")
    time.sleep(2)

    driver.find_element(By.XPATH, "/html/body/ngx-app/div/ngx-pages/ngx-sample-layout/nb-layout/div/div/div/div/div/nb-layout-column/ngx-store-management/div/div/ngx-stores-list/nb-card/nb-card-body/div/ng2-smart-table/table/thead/tr[2]/th[4]/ng2-smart-table-filter/div/default-table-filter/input-filter/input").clear()
    time.sleep(2)
Search_with_wrong_name()


# Searching a store with first letter of store name

@When(u'Admin search a store with first letter of store name')

def Search_with_first_letter_name():
    driver.find_element(By.XPATH, "/html/body/ngx-app/div/ngx-pages/ngx-sample-layout/nb-layout/div/div/div/div/div/nb-layout-column/ngx-store-management/div/div/ngx-stores-list/nb-card/nb-card-body/div/ng2-smart-table/table/thead/tr[2]/th[4]/ng2-smart-table-filter/div/default-table-filter/input-filter/input").send_keys("z")
    time.sleep(2)

    driver.find_element(By.XPATH, "/html/body/ngx-app/div/ngx-pages/ngx-sample-layout/nb-layout/div/div/div/div/div/nb-layout-column/ngx-store-management/div/div/ngx-stores-list/nb-card/nb-card-body/div/ng2-smart-table/table/thead/tr[2]/th[4]/ng2-smart-table-filter/div/default-table-filter/input-filter/input").clear()
    time.sleep(2)

Search_with_first_letter_name()


# Searching a store with middle letter of store name

@When(u'Admin search a store with middle letter of store name')

def Search_with_middle_letter_name():
    driver.find_element(By.XPATH, "/html/body/ngx-app/div/ngx-pages/ngx-sample-layout/nb-layout/div/div/div/div/div/nb-layout-column/ngx-store-management/div/div/ngx-stores-list/nb-card/nb-card-body/div/ng2-smart-table/table/thead/tr[2]/th[4]/ng2-smart-table-filter/div/default-table-filter/input-filter/input").send_keys("o")
    time.sleep(2)

    driver.find_element(By.XPATH, "/html/body/ngx-app/div/ngx-pages/ngx-sample-layout/nb-layout/div/div/div/div/div/nb-layout-column/ngx-store-management/div/div/ngx-stores-list/nb-card/nb-card-body/div/ng2-smart-table/table/thead/tr[2]/th[4]/ng2-smart-table-filter/div/default-table-filter/input-filter/input").clear()
    time.sleep(2)
Search_with_middle_letter_name()


# Searching a store with last letter of store name

@When(u'Admin search a store with last letter of store name')

def Search_with_last_letter_name():
    driver.find_element(By.XPATH, "/html/body/ngx-app/div/ngx-pages/ngx-sample-layout/nb-layout/div/div/div/div/div/nb-layout-column/ngx-store-management/div/div/ngx-stores-list/nb-card/nb-card-body/div/ng2-smart-table/table/thead/tr[2]/th[4]/ng2-smart-table-filter/div/default-table-filter/input-filter/input").send_keys("e")
    time.sleep(2)

    driver.find_element(By.XPATH, "/html/body/ngx-app/div/ngx-pages/ngx-sample-layout/nb-layout/div[1]/div/div/div/div/nb-layout-column/ngx-store-management/div/div/ngx-stores-list/nb-card/nb-card-body/div/ng2-smart-table/table/thead/tr[2]/th[4]/ng2-smart-table-filter/div/default-table-filter/input-filter/input").clear()
    time.sleep(2)
Search_with_last_letter_name()



# Searching a store with correct email

@When(u'Admin search a store with correct email')

def Search_with_correct_email():
    driver.find_element(By.XPATH, "/html/body/ngx-app/div/ngx-pages/ngx-sample-layout/nb-layout/div[1]/div/div/div/div/nb-layout-column/ngx-store-management/div/div/ngx-stores-list/nb-card/nb-card-body/div/ng2-smart-table/table/thead/tr[2]/th[5]/ng2-smart-table-filter/div/default-table-filter/input-filter/input").send_keys("ziaulhaq2@gmail.com")
    time.sleep(2)

    driver.find_element(By.XPATH, "/html/body/ngx-app/div/ngx-pages/ngx-sample-layout/nb-layout/div/div/div/div/div/nb-layout-column/ngx-store-management/div/div/ngx-stores-list/nb-card/nb-card-body/div/ng2-smart-table/table/thead/tr[2]/th[5]/ng2-smart-table-filter/div/default-table-filter/input-filter/input").clear()
    time.sleep(2)
Search_with_correct_email()


# Searching a store with wrong email

@When(u'Admin search a store with wrong email')

def Search_with_wrong_email():
    driver.find_element(By.XPATH, "/html/body/ngx-app/div/ngx-pages/ngx-sample-layout/nb-layout/div/div/div/div/div/nb-layout-column/ngx-store-management/div/div/ngx-stores-list/nb-card/nb-card-body/div/ng2-smart-table/table/thead/tr[2]/th[5]/ng2-smart-table-filter/div/default-table-filter/input-filter/input").send_keys("ziaulhaq12@gmail.com")
    time.sleep(2)

    driver.find_element(By.XPATH, "/html/body/ngx-app/div/ngx-pages/ngx-sample-layout/nb-layout/div/div/div/div/div/nb-layout-column/ngx-store-management/div/div/ngx-stores-list/nb-card/nb-card-body/div/ng2-smart-table/table/thead/tr[2]/th[5]/ng2-smart-table-filter/div/default-table-filter/input-filter/input").clear()
    time.sleep(2)
Search_with_wrong_email()


# Searching a store with first letter of email

@When(u'Admin search a store with first letter of email')

def Search_with_first_letter_email():
    driver.find_element(By.XPATH, "/html/body/ngx-app/div/ngx-pages/ngx-sample-layout/nb-layout/div/div/div/div/div/nb-layout-column/ngx-store-management/div/div/ngx-stores-list/nb-card/nb-card-body/div/ng2-smart-table/table/thead/tr[2]/th[5]/ng2-smart-table-filter/div/default-table-filter/input-filter/input").send_keys("z")
    time.sleep(2)

    driver.find_element(By.XPATH, "/html/body/ngx-app/div/ngx-pages/ngx-sample-layout/nb-layout/div/div/div/div/div/nb-layout-column/ngx-store-management/div/div/ngx-stores-list/nb-card/nb-card-body/div/ng2-smart-table/table/thead/tr[2]/th[5]/ng2-smart-table-filter/div/default-table-filter/input-filter/input").clear()
    time.sleep(2)
Search_with_first_letter_email()


# Searching a store with middle letter of email

@When(u'Admin search a store with middle letter of email')

def Search_with_middle_letter_email():
    driver.find_element(By.XPATH, "/html/body/ngx-app/div/ngx-pages/ngx-sample-layout/nb-layout/div/div/div/div/div/nb-layout-column/ngx-store-management/div/div/ngx-stores-list/nb-card/nb-card-body/div/ng2-smart-table/table/thead/tr[2]/th[5]/ng2-smart-table-filter/div/default-table-filter/input-filter/input").send_keys("g")
    time.sleep(2)

    driver.find_element(By.XPATH, "/html/body/ngx-app/div/ngx-pages/ngx-sample-layout/nb-layout/div/div/div/div/div/nb-layout-column/ngx-store-management/div/div/ngx-stores-list/nb-card/nb-card-body/div/ng2-smart-table/table/thead/tr[2]/th[5]/ng2-smart-table-filter/div/default-table-filter/input-filter/input").clear()
    time.sleep(2)
Search_with_middle_letter_email()


# Searching a store with last letter of email

@When(u'Admin search a store with last letter of email')

def Search_with_last_letter_email():
    driver.find_element(By.XPATH, "/html/body/ngx-app/div/ngx-pages/ngx-sample-layout/nb-layout/div/div/div/div/div/nb-layout-column/ngx-store-management/div/div/ngx-stores-list/nb-card/nb-card-body/div/ng2-smart-table/table/thead/tr[2]/th[5]/ng2-smart-table-filter/div/default-table-filter/input-filter/input").send_keys("m")
    time.sleep(2)

    driver.find_element(By.XPATH, "/html/body/ngx-app/div/ngx-pages/ngx-sample-layout/nb-layout/div/div/div/div/div/nb-layout-column/ngx-store-management/div/div/ngx-stores-list/nb-card/nb-card-body/div/ng2-smart-table/table/thead/tr[2]/th[5]/ng2-smart-table-filter/div/default-table-filter/input-filter/input").clear()
    time.sleep(2)
Search_with_last_letter_email()






# driver.close()




