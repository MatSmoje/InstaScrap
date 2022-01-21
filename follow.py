from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, logging


def follow(usuario, driver): 
    driver.get('https://www.instagram.com/'+usuario)

    errorAlBuscarUsuario = "//*[contains(text(), 'Esta página no está disponible.')]"
    privateUser = "//*[contains(text(), 'Esta cuenta es privada')]"
    seguirSolicitado = "/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div//button[contains(text(), 'Solicitado')]"
    seguir = "/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/button"
    seguirButtonPath = "/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]//button[contains(text(), 'Seguir')]"
    privadoTextContain = "//*[contains(text(), 'Esta cuenta es privada')]"

    if driver.find_elements_by_xpath(errorAlBuscarUsuario):
        logging.info('Cuenta: '+usuario+ ' cerrada/bloqueada/erronea')

    elif driver.find_elements_by_xpath(privateUser):
        logging.info('Cuenta: '+usuario+ ' es cuenta privada')
        #get_info_level_one(usuario)

        if driver.find_element_by_xpath(seguirSolicitado):
            logging.info('Accion seguir a user : '+usuario+ ' ya fue solicitado')

        else:
            logging.info('Solicitud seguimiento a user: '+usuario+ ' realizada')
            driver.find_element_by_xpath(seguir).click()

    else: #usuario publico o ya seguido     

        try:
            if driver.find_element_by_xpath(seguirButtonPath) and not driver.find_elements_by_xpath(privadoTextContain):
                driver.find_element_by_xpath(seguirButtonPath).click()
                logging.info('Start following - Public user '+usuario)

        except:
            logging.info('Already followed - Private user: '+usuario)
    return driver