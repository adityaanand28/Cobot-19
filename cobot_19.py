import aiml
import os
import requests, json
import bs4
from selenium import webdriver

kernel = aiml.Kernel()




kernel.bootstrap(learnFiles = "cobot_19.xml", commands = "LOAD BASIC CHAT")
   

# kernel now ready for use
url='https://www.mohfw.gov.in/'

while True:
    respond = input("USER > ")

    if respond.lower() == "bye" :
        print("Would you like to give us a feedback.")

        respond = input("> ")
        if respond.lower() == "yes" :
    
            respond = input("Feedback : ")

            print("Thanks, for your feedback sir !")

            break
        
        if respond.lower() == "no" :

            print("Look like you dont enjoy our service . We are improving! , Hope to see you back!")
            break

        else :

            print("Thanks for choosing us . We hope you will come back soon.")
            break
    elif respond.lower() =="stats":
        url = 'https://www.mohfw.gov.in/data/datanew.json'
        res = requests.get(url)
        res = res.json()
        user_state = input("Enter State :")
        for str in res: 
            if(user_state.lower().strip() == str['state_name'].lower().strip()):
                print("PHΦNEIX COBOT > Active cases are:",str['active'])
   
    print("PHΦNEIX COBOT > " + kernel.respond(respond))
