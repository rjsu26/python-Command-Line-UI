from selenium import webdriver
from getpass import getpass

browser = webdriver.Chrome()
browser.get('https://www.facebook.com/')

def get_details():
    usr = input("Enter  usr name:")
    pwd = getpass("password: ")


def send_details(usr,pwd):
    usr_nm = browser.find_element_by_id('email')
    pass_nm = browser.find_element_by_id('pass')
    login_btn =browser.find_element_by_id('u_0_2')
    usr_nm.send_keys(usr)
    pass_nm.send_keys(pwd)
    login_btn.submit()

def do_facebook():
    get_details()
    send_details(usr,pwd)