import time,json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def userLogin(driver,mPinIn) : 
    user_email = driver.find_element(By.ID,'login_email')
    user_email.send_keys("sanket.shelke")

    domain = Select(driver.find_element(By.NAME,"subdomain"))
    domain.select_by_value("@neosoftmail.com")

    isInValid = True
    while isInValid:
        if mPinIn :
            Pin = mPinIn
            mPinIn = ''
        else : 
            Pin = input("Enter mPin : ")
            
        mPin = list(map(int,str(Pin)))
        mPinArray = driver.find_elements(By.CLASS_NAME,"otp-input")
        for pin,value in zip(mPinArray,mPin) : 
            pin.send_keys(value)

        driver.find_element(By.XPATH,'//*[@id="btn_do_login"]').click()
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.ID, "loading-wrapper")))
        isInValid = driver.current_url != 'https://1-thing.in/#/home'

    time.sleep(5)
    local_storage = driver.execute_script('return JSON.stringify(window.localStorage);')

    with open("session.json", 'w') as file : 
        json.dump(local_storage,file)



# Function to scroll into view and click an element
def scroll_and_click(xpath,driver):
    wait = WebDriverWait(driver, 10)
    WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.ID, "loading-wrapper")))
    element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    element.click()
