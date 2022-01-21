import logging, time
import bcolors as color
import login, follow, get_information



########  CONFIGURATIONS  ########
logging.basicConfig(
    filename='InstagramScraper.log', 
    encoding='utf-8', 
    level=logging.INFO,
    format='%(asctime)s %(levelname)-8s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')


 ########  USERS TO SEE  ########   
usuario = ['Cyberkaia','ivahen','goodguychile','fenixreview','danipineg','juegosgori']



driver = login.login()
#follow.follow('matias_smoje', driver)
for user in usuario:
    file = open('instagramData.txt','a+')
    follow.follow(user,driver)
    get_information.get_basic_info(user,driver)

