from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import json
from selenium.webdriver.common.action_chains import ActionChains
from helper import userLogin,scroll_and_click
import argparse
from sys import exit
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Get aruguments Values and assign to variables 
task_descriptions = {
        1: 'Working on ERM',
        2: 'Working on Exxon'
    }
# parser = argparse.ArgumentParser()
task_info = '\n'.join([f"  {code}: {desc}" for code, desc in task_descriptions.items()])
    
parser = argparse.ArgumentParser(
        description=f"Task Management System\n\nTask codes:\n{task_info}",
        formatter_class=argparse.RawTextHelpFormatter
    )
parser.add_argument('-p' ,type=int,help='Pass MPin')
parser.add_argument('-l', action='store_true', help='Last Week fill')
parser.add_argument(
        '-t', '--task',
        type=int,
        choices=task_descriptions.keys(),
        help='Task code to execute'
    )
args = parser.parse_args()
mPinIn = args.p
last_week = args.l
task = args.task

print(task)
if task : 
    if task == 1 : 
        print("test 1")
        task_name = 'Working on ERM'
    elif task == 2 :
        task_name = 'Working on Exxon'
else :
    print("test2")
    task_name = 'Working on TXC'


driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://1-thing.in/")

with  open("session.json") as file: 
    jsonData = json.load(file)

print(jsonData)
driver.execute_script("""
    var data = JSON.parse(arguments[0]);
    for (var key in data) {
        window.localStorage.setItem(key, data[key]);
    }
""", jsonData)
driver.get("https://1-thing.in/#/home")
    
time.sleep(5)
isLogin = driver.current_url == 'https://1-thing.in/#/home'

if not(isLogin) :
    userLogin(driver,mPinIn)
if isLogin : 
    print("Login Successful")
    workspace = driver.find_element(By.XPATH,'//*[@id="app"]/div/header/div/div[2]/div[1]/div/span')
    workspace.click()

    accentivWS = driver.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div/div[1]/div[2]/div[2]/div/div/div[1]/div/span/i')
    accentivWS.click()
    time.sleep(2)
    # driver.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/span').click()
    # driver.find_element(By.XPATH,'//*[@id="app"]/div/header/div/div[1]/div').click()
    # driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/nav/ul/li[4]/a').click()
    # driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[1]/div/div[1]/div[2]').click()
    
    scroll_and_click('//*[@id="app"]/div/div[1]/div[2]/span',driver)
    scroll_and_click('//*[@id="app"]/div/header/div/div[1]/div',driver)
    scroll_and_click('//*[@id="app"]/div/div[2]/div[2]/nav/ul/li[4]/a',driver)
    scroll_and_click('//*[@id="app"]/div/div[2]/div[1]/div/div[1]/div[2]',driver)


    if last_week:
        scroll_and_click('//*[@id="app"]/div/div[2]/div[1]/div/div[1]/div[4]',driver)
    # logWeek = driver.find_elements(By.CLASS_NAME,'dhx_scale_holder')
    logWeek = driver.find_elements(By.XPATH, '//div[contains(@data-column-index, "0") or contains(@data-column-index, "1") or contains(@data-column-index, "2") or contains(@data-column-index, "3") or contains(@data-column-index, "4")]')

    i = 0
    for day in logWeek :
        if i == 5 :
            break
        i = i + 1
        actionChains = ActionChains(driver)
        actionChains.double_click(day).perform()
        select_task = Select(driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[2]/div[2]/select'))
        select_task.select_by_visible_text(task_name)
        select_intime = Select(driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[4]/div[2]/select[1]'))
        select_intime.select_by_visible_text("09:30 AM")
        select_outtime = Select(driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[4]/div[2]/select[5]'))
        select_outtime.select_by_visible_text("06:30 PM")

        driver.find_element(By.XPATH,'/html/body/div[1]/div[4]/div[2]').click()
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.ID, "loading-wrapper")))

input("Press any key to exit")
time.sleep(10)

    




