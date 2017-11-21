from selenium import webdriver
import time

#login using email and pw, readies to spam first chat
def login(email, pw):
    login_enter = driver.find_element_by_id('signinUserNameInput')
    login_enter.send_keys(email)
    pass_enter = driver.find_element_by_id('signinPasswordInput')
    pass_enter.send_keys(pw)
    driver.find_element_by_css_selector('#signin > div > form > button').click()
    driver.implicitly_wait(4)
    driver.find_element_by_css_selector('#tray > div.tray-list > div.chats.groupme-list > button:nth-child(2) > div > div.list-body > div > div > p > span:nth-child(3)').click()

#start spamming
def start(message, num, driver):
    for i in range(0, num):
        driver.find_element_by_css_selector("#chats > div > div.chat-content > div > div.chat-input > div > div.composer-layout > div.composer-wrapper > div").send_keys(message)
        driver.implicitly_wait(4)
        time.sleep(1)
        driver.find_element_by_css_selector("#chats > div > div.chat-content > div > div.chat-input > div > div.composer-layout > div.composer-wrapper > div").send_keys(u'\ue007')


# cute interface for the lazy
if __name__ == "__main__":
    
    #go to groupMe
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome('C:\\Users\\cjlro\\Documents\\FALL2017\\spammer\\chromedriver.exe'
                              , chrome_options=options)
    driver.get('https://web.groupme.com/signin')
    
    email = input("Enter GroupMe email address: ")
    pw = input("Enter GroupMe pw: ")
    login(email, pw)
        
    message = input("Enter message: ")
    num = int(input("How many?: "))
    start(message, num, driver)
    
    goAgain = True
    while(goAgain):
        
        decision = input("again?: ")
        if(decision != "y" or decision != "Y"):
            goAgain = False
        start(message, num, driver)