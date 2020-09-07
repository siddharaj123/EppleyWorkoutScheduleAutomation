from selenium import webdriver
from selenium .webdriver.common.keys import Keys
browser = webdriver.Chrome('/Users/siddharajvaghela/Downloads/chromedriver')
browser.get('https://www.imleagues.com/spa/fitness/4395e0c781af4905a4088a9561509399/home')

week = browser.find_element_by_xpath("/html/body/div[3]/div[1]/div[11]/div/div[2]/div/div[1]/div[2]/div[1]/div/div[5]/week-calendar/div[1]/div[1]/table/tbody/tr/td[1]/table/tbody/tr/td[1]/div/button[2]")
week.click()

workout = browser.find_element_by_xpath("/html/body/div[3]/div[1]/div[11]/div/div[2]/div/div[1]/div[2]/div[1]/div/div[5]/week-calendar/div[2]/div[2]/div/div[1]/a/div/div[1]")
workout.click()

signUp = browser.find_element_by_xpath("/html/body/div[3]/div[1]/div[11]/div/div[2]/div/div[1]/div[2]/div[1]/div/div[3]/div/div/div[2]/div/a")
signUp.click()

selectSchool = browser.find_element_by_xpath("/html/body/ng-include/div/div[4]/div/div[1]/div[2]/div[1]/div[2]/div/div/div/form/div[1]/div[1]/div/div/button")
selectSchool.click()

typeSchool = browser.find_element_by_xpath("/html/body/ng-include/div/div[4]/div/div[1]/div[2]/div[1]/div[2]/div/div/div/form/div[1]/div[1]/div/div/div/div/input")
typeSchool.send_keys("University of Maryland")

UMD = browser.find_element_by_xpath("/html/body/ng-include/div/div[4]/div/div[1]/div[2]/div[1]/div[2]/div/div/div/form/div[1]/div[1]/div/div/div/ul/li[1722]/a")
UMD.click()
Directory_ID = browser.find_element_by_id("username")
Directory_ID.send_keys("svaghela")
Password = browser.find_element_by_id("password")
Password.send_keys("WKXd5UDv#$UDy9*")
LogIn = browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/form/div[4]/button")
LogIn.click()