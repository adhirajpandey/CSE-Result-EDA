import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


output_dir = "E:\\MIET EDA\\results\\DS"

path = "C:\\Users\\Adhiraj\\Documents\\Projects\\Ongoing\\Miet Result EDA\\chromedriver.exe"
base_query_url = "https://erp.aktu.ac.in/webpages/oneview/oneview.aspx"

rollnumbers = [x for x in range(2000681540001, 2000681540051)]

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(executable_path = path, options = options)
driver.get(base_query_url)
driver.maximize_window()
time.sleep(1)

print(rollnumbers)

for rollnumber in rollnumbers:
    
    driver.get(base_query_url)
    time.sleep(1)
    
    txtbox = driver.find_element(By.XPATH, '//input[@name="txtRollNo"]')
    txtbox.send_keys(rollnumber)
    time.sleep(2)

    captcha = driver.find_element(By.XPATH, "//iframe[starts-with(@name, 'a-') and starts-with(@src, 'https://www.google.com/recaptcha')]")
    captcha.click()
    time.sleep(5)

    submitbutton = driver.find_element(By.XPATH, '//input[@type="submit"]')
    submitbutton.click()
    time.sleep(5)

    # printbtn = driver.find_element(By.XPATH, '//a[@onclick="return PrintDiv();"]')
    ps = driver.page_source

    with open(f'{output_dir}\\{rollnumber}.html', 'w', encoding = 'utf-8') as f:
        f.write(ps)
    
    print(f'Roll Number - {rollnumber} Done')