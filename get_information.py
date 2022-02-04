from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date
import logging
import bcolors as color
import json
import dataSchema

def get_basic_info(usuario,driver):
    fileName = 'test.json'
    data = {}
    xPathDataPublication = "/html/body/div[1]/section/main/div/header/section/ul"
    basicInfo = driver.find_elements_by_xpath(xPathDataPublication)#.text
    
    for x in basicInfo:
        datosIg = x.text.split('\n')
        information = {
            "time": str(date.today()), 
            "user":usuario,
            "publications": datosIg[0].split(' ')[0] ,
            "followes": datosIg[1].split(' ')[0] ,
            "following": datosIg[2].split(' ')[0]
              }
        print(datosIg)
        
        #print(color.OKGREEN + usuario + '\n' + color.ENDC + ' ' + datosIg[0] + datosIg[1])
        dataSchema.add_data(information)
    
    
    return driver, basicInfo

    #"followes": "24,1k" -> string replace k x 000 ->24,1000 replace = 