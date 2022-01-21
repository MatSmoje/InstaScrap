import json
import logging



def add_data(dataArray):
    filename = 'instagramData.txt'

    try:
        with open(filename, "r") as file:
            data = json.load(file)
            
    except:
        print("archivo se encontraba vacío")
        logging.info('Archivo: '+ filename + 'Se encontraba vacío.')
        data = []

    finally:
        data.append(dataArray)
 
        with open(filename, "w") as file:
            json.dump(data, file)
    