from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
option = webdriver.ChromeOptions()
option.add_argument('--headless')
option.add_argument("--disable-logging")
option.add_experimental_option('excludeSwitches', ['enable-logging'])
option.add_argument("--incognito")
chromedriver = 'D:\\iamkunal9\\selenium\\instagram_followers\\chromedriver.exe' # Add your chromedriver path!!! https://chromedriver.chromium.org/downloads check your chrome version by going on chrome://version
option.binary_location = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe' ## comment out this if you use chrome 
s = Service(chromedriver)
driver = webdriver.Chrome(service=s, options=option)
wait = WebDriverWait(driver, 30)
print("Welcome!!")


userName = "Your User Name" # get it from https://app.turbomedia.io/login
passWord = "Your passoword"

driver.get("https://app.turbomedia.io/login")
username = driver.find_element(By.XPATH, "//input[@placeholder='Your Instagram Username']")
username.send_keys(userName)

password = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
password.send_keys(passWord)
password.send_keys(Keys.ENTER)

try:

    driver.find_element(By.XPATH,"/html/body/section/div/div/div/div[2]/div[3]/div/div[1]/div/div/div/form/div[2]/button").click()
except:
    print("Daily Quota Exceeded Please try again after 24 hrs or wrong username/password")
    exit()
try:
    for i in range(0,10):
        time.sleep(1)
        wait.until(EC.invisibility_of_element_located((By.XPATH, '/html/body/div[1]')))
        time.sleep(2)
        driver.find_element(By.XPATH, '/html/body/section/div/div/div/div[1]/div[2]/div[3]/div[2]/div[1]/a').click()
        print("closing the follow tab")
        driver.switch_to.window(driver.window_handles[1])
        driver.close()

        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)

        wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/section/div/div/div/div[1]/div[2]/div[3]/div[2]/div[2]/form/button')))
        time.sleep(1)
        driver.find_element(By.XPATH, "/html/body/section/div/div/div/div[1]/div[2]/div[3]/div[2]/div[2]/form/button").click()

    time.sleep(2)
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/section/div/div/div/div[1]/div[2]/div/form/button')))
    driver.find_element(By.XPATH,"/html/body/section/div/div/div/div[1]/div[2]/div/form/button").click()

    print("The Followers will be credited to your account shortly!!!")
except:
    print("some error occured please try again!!")
