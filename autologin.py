from selenium import webdriver
from getpass import getpass

username = "ammarkhan375@gmail.com"
password = "spencer.nk"

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://www.levnycart.com/login.php")

# username_textbox = driver.find_element_by_id("email")
username_textbox = driver.find_element_by_name("uname")
username_textbox.send_keys(username)

# password_textbox = driver.find_element_by_id("pass")
password_textbox = driver.find_element_by_name("password")
password_textbox.send_keys(password)

login_button = driver.find_element_by_name("login")
login_button.click()

