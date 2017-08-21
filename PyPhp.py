
import urllib2, urllib
import time as t

a = 0

path = 'https://letsmakeit.000webhostapp.com/HelloPK/PhPy/test.php'  # the url you want to POST to

path1 = "https://letsmakeit.000webhostapp.com/HelloPK/PhPy/nodeMcu.php"
path2 = "http://192.168.42.194/text.php"
path3 = "http://192.168.42.194/ServerFiles/pavan.php"

while True:

    a += 1
    mydata = [('value', a)]  # The first is the var name the second is the value
    mydata = urllib.urlencode(mydata)
    print "myData is: " + mydata
    req = urllib2.Request(path3, mydata)
    req.add_header("Content-type", "application/x-www-form-urlencoded")
    page = urllib2.urlopen(req).read()
    print "Page is :" + page

    t.sleep(2)

'''
import requests

path = 'https://letsmakeit.000webhostapp.com/HelloPK/PhPy/test.php'  # the url you want to POST to
userdata = {"firstname": "John", "lastname": "Doe", "password": "jdoe123"}
resp = requests.post(path, params=userdata)
print resp
'''
