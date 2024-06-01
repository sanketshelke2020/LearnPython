from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import json
from selenium.webdriver.common.action_chains import ActionChains
from helper import userLogin, scroll_and_click
import argparse
from sys import exit
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Get Task List
with open("tasklist.json", "r") as file:
    data_dict = json.load(file)
task_descriptions = data_dict

task_info = "\n".join([f"  {code}: {desc}" for code, desc in task_descriptions.items()])
parser = argparse.ArgumentParser(
    description=f"Task Management System\n\nTask codes:\n{task_info}",
    formatter_class=argparse.RawTextHelpFormatter,
)
parser.add_argument("-p", type=int, help="Pass MPin")
parser.add_argument("-u", action="store_true", help="Update Task List")
parser.add_argument("-a", type=str, help="Add New Task")
parser.add_argument("-l", action="store_true", help="Last Week fill")
parser.add_argument(
    "-t",
    "--task",
    type=int,
     choices = [eval(i) for i in list(task_descriptions.keys())],
    help="Task code to execute",
)
args = parser.parse_args()
mPinIn = args.p
last_week = args.l
task = args.task
add = args.a
update = args.u


if task:
    task_name = task_descriptions[str(task)]
else:
    print("Please Select Task")
    exit()

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://1-thing.in/")

with open("session.json") as file:
    jsonData = json.load(file)

print(jsonData)
driver.execute_script(
    """
    var data = JSON.parse(arguments[0]);
    for (var key in data) {
        window.localStorage.setItem(key, data[key]);
    }
""",
    jsonData,
)
driver.get("https://1-thing.in/#/home")

time.sleep(5)
isLogin = driver.current_url == "https://1-thing.in/#/home"

if not (isLogin):
    userLogin(driver, mPinIn)
if isLogin:
    print("Login Successful")
    workspace = driver.find_element(
        By.XPATH, '//*[@id="app"]/div/header/div/div[2]/div[1]/div/span'
    )
    workspace.click()

    accentivWS = driver.find_element(
        By.XPATH,
        '//*[@id="app"]/div/div[1]/div[2]/div/div[1]/div[2]/div[2]/div/div/div[1]/div/span/i',
    )
    accentivWS.click()
    time.sleep(2)
    scroll_and_click('//*[@id="app"]/div/div[1]/div[2]/span', driver) 
    scroll_and_click('//*[@id="app"]/div/header/div/div[1]/div', driver) #open sidebar

# Add Task 
    if add : 
        scroll_and_click('//*[@id="app"]/div/div[2]/div[2]/nav/ul/li[2]/a/img[2]', driver) # task click 
        scroll_and_click('//*[@id="app"]/div/header/div/div[1]/div', driver) # close sidebar
        # time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.ID, "loading-wrapper")))
 
        driver.find_element(By.XPATH,'//*[@id="t-step-2"]/div[1]').click()
        scroll_and_click('//*[@id="collapse-51266"]/div/div[1]/div/a', driver)
        driver.find_element(By.XPATH,'//*[@id="frm-add-task"]/input').send_keys(add);
        driver.find_element(By.XPATH,'//*[@id="51266"]/div/div[2]/div/div[2]/div/div/div[2]/input').click();
        print(f"************ Added Task : {add}**************")
        input("Press any key to exit")
        exit()

# Getting Task List 
    if update : 
        scroll_and_click('//*[@id="app"]/div/div[2]/div[2]/nav/ul/li[2]/a/img[2]', driver) # task click 
        scroll_and_click('//*[@id="app"]/div/header/div/div[1]/div', driver) # close sidebar
        # time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.ID, "loading-wrapper")))
 
        driver.find_element(By.XPATH,'//*[@id="t-step-2"]/div[1]').click()
        task_div = driver.find_element(By.XPATH,'//*[@id="51266"]')
        

        elements = task_div.find_elements(By.CSS_SELECTOR, '.task-list-title-new label')
        for e,i in enumerate(elements):
            print(i.get_attribute("innerHTML").strip())
            data_dict[e] =  i.get_attribute("innerHTML").strip()

    
     
        print(data_dict)
        with open("tasklist.json",'w') as t : 
            json.dump(data_dict,t)

        print("********Updated Task List***********")
        exit()


    scroll_and_click('//*[@id="app"]/div/div[2]/div[2]/nav/ul/li[4]/a', driver) #schedular click
    scroll_and_click('//*[@id="app"]/div/div[2]/div[1]/div/div[1]/div[2]', driver)

    if last_week:
        scroll_and_click('//*[@id="app"]/div/div[2]/div[1]/div/div[1]/div[4]', driver)
    # logWeek = driver.find_elements(By.CLASS_NAME,'dhx_scale_holder')
    logWeek = driver.find_elements(
        By.XPATH,
        '//div[contains(@data-column-index, "0") or contains(@data-column-index, "1") or contains(@data-column-index, "2") or contains(@data-column-index, "3") or contains(@data-column-index, "4")]',
    )

    i = 0
    for day in logWeek:
        if i == 5:
            break
        i = i + 1
        actionChains = ActionChains(driver)
        actionChains.double_click(day).perform()
        select_task = Select(
            driver.find_element(
                By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/select"
            )
        )
        select_task.select_by_visible_text(task_name)
        select_intime = Select(
            driver.find_element(
                By.XPATH, "/html/body/div[1]/div[2]/div[4]/div[2]/select[1]"
            )
        )
        select_intime.select_by_visible_text("09:30 AM")
        select_outtime = Select(
            driver.find_element(
                By.XPATH, "/html/body/div[1]/div[2]/div[4]/div[2]/select[5]"
            )
        )
        select_outtime.select_by_visible_text("06:30 PM")

        driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[2]").click()
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.ID, "loading-wrapper"))
        )

input("Press any key to exit")
