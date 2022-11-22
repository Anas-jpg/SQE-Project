from selenium.webdriver.common.keys import Keys
import time
from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from pytest_bdd import scenario, given, when, then

driver: WebDriver = webdriver.Chrome("C:\Chrome\\chromedriver.exe")

driver.get("http://localhost/register")
driver.maximize_window()

@given(u': I have registered my account in shopizer')
def registerationportal():
    driver.get("http://localhost/register")
    time.sleep(1)
    driver.find_element(By.NAME, "email").send_keys("hassan@123.com")
    time.sleep(0.75)
    driver.find_element(By.NAME, "password").send_keys("Malik@12345")
    time.sleep(0.75)
    driver.find_element(By.NAME, "repeatPassword").send_keys("Malik@12345")
    time.sleep(0.75)
    driver.find_element(By.NAME, "firstName").send_keys("Hassan")
    time.sleep(0.75)
    driver.find_element(By.NAME, "lastName").send_keys("Murtaza")
    time.sleep(0.75)
    ele=driver.find_element(By.XPATH,"//*[@id='root']/div[4]/div/div/div/div/div[2]/div[2]/div/div/form/div[6]/select")
    time.sleep(0.75)
    ele.click()
    el=driver.find_element(By.XPATH,"//*[@id='root']/div[4]/div/div/div/div/div[2]/div[2]/div/div/form/div[6]/select/option[2]")
    time.sleep(0.75)
    el.click()
    time.sleep(0.75)
    driver.execute_script("window.scrollBy(0,400)","")
    e1=driver.find_element(By.XPATH,"//*[@id='root']/div[4]/div/div/div/div/div[2]/div[2]/div/div/form/div[7]/select")
    time.sleep(0.75)
    e1.click()
    e2=driver.find_element(By.XPATH,"//*[@id='root']/div[4]/div/div/div/div/div[2]/div[2]/div/div/form/div[7]/select/option[7]")
    time.sleep(0.75)
    e2.click()
    element=driver.find_element(By.XPATH,"//*[@id='root']/div[4]/div/div/div/div/div[2]/div[2]/div/div/form/div[8]/button")
    time.sleep(2)
    element.click()
registerationportal()

@When(u'I leave first name empty')
def empty_firstname():
    time.sleep(1.75)
    anas = driver.find_element(By.XPATH, "//*[@id='root']/div[4]/div/div/div/div/div/div[3]/div[1]/button/h3")
    time.sleep(0.75)
    anas.click()
    time.sleep(0.75)
    driver.find_element(By.NAME, "shipFirstName").send_keys("")
    time.sleep(0.75)
    driver.find_element(By.NAME, "shipLastName").send_keys("Malik")
    time.sleep(0.75)
    driver.find_element(By.NAME, "shipCompany").send_keys("Educative")
    time.sleep(0.75)
    driver.find_element(By.NAME, "shipAddress").send_keys("street no 2")
    driver.execute_script("window.scrollBy(0,250)", "")
    hassan = driver.find_element(By.XPATH, "//*[@id='root']/div[4]/div/div/div/div/div/div[3]/div[2]/div/div/form/div[1]/div[5]/div/select")
    hassan.click()
    driver.execute_script("window.scrollBy(0,250)", "")
    hanan = driver.find_element(By.XPATH, "//*[@id='root']/div[4]/div/div/div/div/div/div[3]/div[2]/div/div/form/div[1]/div[5]/div/select/option[6]")
    hanan.click()
    time.sleep(0.75)
    driver.find_element(By.NAME, "shipStateProvince").send_keys("Punjab")
    time.sleep(0.75)
    driver.find_element(By.NAME, "shipCity").send_keys("Lhr")
    time.sleep(0.75)
    driver.find_element(By.NAME, "shipPostalCode").send_keys("54000")
    time.sleep(0.75)
    driver.find_element(By.NAME, "shipPhone").send_keys("0333231116")
    time.sleep(0.75)
    zia = driver.find_element(By.XPATH,"//*[@id='root']/div[4]/div/div/div/div/div/div[3]/div[2]/div/div/form/div[2]/div/button")
    time.sleep(2)
    zia.click()
empty_firstname()

@When(u'I leave last name empty')
def empty_secondname():
    time.sleep(1.75)
    driver.get("http://localhost/my-account")
    anas = driver.find_element(By.XPATH, "//*[@id='root']/div[4]/div/div/div/div/div/div[3]/div[1]/button/h3")
    time.sleep(0.75)
    anas.click()
    time.sleep(0.75)
    driver.find_element(By.NAME, "shipFirstName").send_keys("Malik")
    time.sleep(0.75)
    driver.find_element(By.NAME, "shipLastName").send_keys("")
    time.sleep(0.75)
    driver.find_element(By.NAME, "shipCompany").send_keys("Educative")
    time.sleep(0.75)
    driver.find_element(By.NAME, "shipAddress").send_keys("street no 2")
    driver.execute_script("window.scrollBy(0,250)", "")
    hassan = driver.find_element(By.XPATH, "//*[@id='root']/div[4]/div/div/div/div/div/div[3]/div[2]/div/div/form/div[1]/div[5]/div/select")
    hassan.click()
    driver.execute_script("window.scrollBy(0,250)", "")
    hanan = driver.find_element(By.XPATH, "//*[@id='root']/div[4]/div/div/div/div/div/div[3]/div[2]/div/div/form/div[1]/div[5]/div/select/option[6]")
    hanan.click()
    time.sleep(0.75)
    driver.find_element(By.NAME, "shipStateProvince").send_keys("Punjab")
    time.sleep(0.75)
    driver.find_element(By.NAME, "shipCity").send_keys("Lhr")
    time.sleep(0.75)
    driver.find_element(By.NAME, "shipPostalCode").send_keys("54000")
    time.sleep(0.75)
    driver.find_element(By.NAME, "shipPhone").send_keys("0333231116")
    time.sleep(0.75)
    zia = driver.find_element(By.XPATH,"//*[@id='root']/div[4]/div/div/div/div/div/div[3]/div[2]/div/div/form/div[2]/div/button")
    time.sleep(2)
    zia.click()
empty_secondname()

@When(u'I give valid inputs')
def add_address1():
    time.sleep(2)
    driver.get("http://localhost/my-account")
    anas=driver.find_element(By.XPATH,"//*[@id='root']/div[4]/div/div/div/div/div/div[3]/div[1]/button/h3")
    time.sleep(0.75)
    anas.click()
    time.sleep(0.75)
    driver.find_element(By.NAME, "shipFirstName").send_keys("Malik")
    time.sleep(0.75)
    driver.find_element(By.NAME, "shipLastName").send_keys("Hassan")
    time.sleep(0.75)
    driver.find_element(By.NAME, "shipCompany").send_keys("Educative")
    time.sleep(0.75)
    driver.find_element(By.NAME, "shipAddress").send_keys("street no 2")
    driver.execute_script("window.scrollBy(0,250)", "")
    hassan=driver.find_element(By.XPATH, "//*[@id='root']/div[4]/div/div/div/div/div/div[3]/div[2]/div/div/form/div[1]/div[5]/div/select")
    hassan.click()
    driver.execute_script("window.scrollBy(0,250)", "")
    hanan=driver.find_element(By.XPATH, "//*[@id='root']/div[4]/div/div/div/div/div/div[3]/div[2]/div/div/form/div[1]/div[5]/div/select/option[6]")
    hanan.click()
    time.sleep(0.75)
    driver.find_element(By.NAME, "shipStateProvince").send_keys("Punjab")
    time.sleep(0.75)
    driver.find_element(By.NAME, "shipCity").send_keys("Lahore")
    time.sleep(0.75)
    driver.find_element(By.NAME, "shipPostalCode").send_keys("54000")
    time.sleep(0.75)
    driver.execute_script("window.scrollBy(0,200)", "")
    driver.find_element(By.NAME, "shipPhone").send_keys("0333231116")
    time.sleep(0.75)
    zia=driver.find_element(By.XPATH, "//*[@id='root']/div[4]/div/div/div/div/div/div[3]/div[2]/div/div/form/div[2]/div/button")
    time.sleep(2)
    zia.click()
    driver.execute_script("window.scrollBy(0,300)", "")
    time.sleep(4)
    driver.find_element(By.XPATH, "//*[@id='root']/div[4]/div/div/div/div/div/div[5]/div[1]/button/h3").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//*[@id='root']/div[4]/div/div/div/div/div/div[5]/div[2]/div/div/form/div/div/button").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='root']/div[5]/div/div/p/a[2]").click()
add_address1()