# importing the requests library
import requests
import time as tp
import serial

# api-endpoint
URL = "http://192.168.42.194/text.php"
URL_1 = "http://192.168.42.194/ServerFiles/pavan.php"

ser = serial.Serial('/dev/ttyUSB0', 9600)

a = 0
# location given here
while True:

    SerialDat = ser.readline()

    a += 1
    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'value': a}

    # sending get request and saving the response as response object
    r = requests.get(url=URL_1, params=PARAMS)

    # extracting data in json format
    #data = r.json()

    print r
    tp.sleep(3)

