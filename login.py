from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import passwd as pwd
import time



def login():
    link = 'https://www.instagram.com/'
    BttnLogIn = "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div"
    driver_path = r'C:\Users\matia\Downloads\chromedriver_win32\chromedriver.exe'
    checkLogged = "/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/a"
    
    options = Options()
    options.add_argument("user-data-dir=C:\\Users\\matia\\Desktop\\M\\Python\\Instagram Scraper\\Cookies")
    driver = webdriver.Chrome(driver_path, chrome_options=options)
    
    wait = WebDriverWait(driver, 3)
    presence = EC.presence_of_element_located
    visible = EC.visibility_of_element_located

    driver.get(link)
    try:
        if(driver.find_element_by_xpath(checkLogged)):
            pass
    except:
            
        wait.until(visible((By.NAME, "username")))
        wait.until(visible((By.NAME, "password")))

        logUser = driver.find_element_by_name("username")
        logUser.click()
        logUser.send_keys(pwd.user)
    
        logPasswd = driver.find_element_by_name("password")
        logPasswd.click()
        logPasswd.send_keys(pwd.passwd)

        driver.find_element_by_xpath(BttnLogIn).click()
        time.sleep(10)
    return driver