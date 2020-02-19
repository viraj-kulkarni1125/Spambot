from selenium import webdriver
import time
import unittest 
import pyautogui as py
import pyperclip 

class SpamBot(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
            
    def tearDown(self):
        self.browser.quit()

    def test_spambot(self):
        
        #Gathering input and logging in
        self.browser.get('https://www.messenger.com/')
        py.hotkey('alt', 'space')
        py.hotkey('x')
        py.hotkey('alt', 'tab')
        time.sleep(1)
        print("Input your login id (Email or phone no.)")
        login_id=input()
        print("Input your password")
        password=input()
        print("Input the full name of your target")
        target=input()
        print("Input the message you wish to spam your target with")
        message=input()
        print("Input how many messages you want to spam your target with")
        message_count=int(input())
        py.hotkey('alt', 'tab')
        

        #Simulate user input logging into messenger       
        usernameLoginInputBox = self.browser.find_element_by_id('email')
        usernameLoginInputBox.click()
        usernameLoginInputBox.send_keys(login_id)
        
        passwordLoginInputBox = self.browser.find_element_by_id('pass')
        passwordLoginInputBox.click()
        passwordLoginInputBox.send_keys(password)
        
        loginButton = self.browser.find_element_by_id('loginbutton')
        loginButton.click()
        time.sleep(1)

        #Finding the target
        time.sleep(2)
        py.moveTo(108,199, duration=0.5)
        py.click(108, 199)
        py.typewrite(target)
        py.moveTo(240, 354, duration=0.5)
        py.click()
        py.moveTo(978, 996, duration=2)
        py.click()
        
        #Spamming
        pyperclip.copy(message)
        count=0
        while count != message_count:
            py.hotkey("ctrl", "v")    
            time.sleep(0.2)
            py.hotkey("enter")
            count = count + 1     
        
        time.sleep(10)
        print("Spammed" '"',target, '"','with the message','"', message,'"', "for a number of", message_count, "time(s)")
        

if __name__ == '__main__':
    unittest.main(warnings='ignore')
