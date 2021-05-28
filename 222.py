
import my_cred
from pages import *
from selenium import webdriver
from time import sleep

browser = webdriver.Firefox()
browser.implicitly_wait(5)

home_page = HomePage(browser)
login_page = home_page.go_to_login_page()
login_page.login(my_cred.my_login, my_cred.my_pass)


#browser.get('https://www.instagram.com/')
#username_input = browser.find_element_by_css_selector("input[name='username']")
#password_input = browser.find_element_by_css_selector("input[name='password']")

#username_input.send_keys(my_cred.my_login)
#password_input.send_keys(my_cred.my_pass)
#login_button = browser.find_element_by_css_selector("button[type='submit']")
#login_button.click()
sleep(5)
button2 = browser.find_element_by_css_selector("button[class='sqdOP yWX7d    y3zKF     ']")
button2.click()
sleep(5)
button3 = browser.find_element_by_css_selector("button[class='aOOlW   HoLwm ']")
button3.click()
#browser.close()