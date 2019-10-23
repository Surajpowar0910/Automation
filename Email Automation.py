# Created by: Suraj Powar
# Date: 12/10/2019
# Description: The below code is build using python and selenium for purpose of automation. It will go to web address of Google email and sign in for you and send an email with no body but just a subject to sender you specify in the code.
# The motive is to easily sign in into the gmail and do automated task.



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

email = '' #Enter your google email address.
password = '' #Enter your password of google email.
reciever = '' #Enter the email address of the person whom to send an email.

browser = webdriver.Chrome()
browser.get('https://www.gmail.com')

element = browser.find_element_by_xpath('//*[@id="identifierId"]')
element.send_keys(email)
time.sleep(1)

next_element = browser.find_element_by_xpath('//*[@id="identifierNext"]/span/span')
next_element.click()

browser.implicitly_wait(30)

element_2 = browser.find_element_by_css_selector("#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input")
element_2.send_keys(password)

browser.implicitly_wait(20)

element_3 = browser.find_element_by_xpath('//*[@id="passwordNext"]/span/span')
element_3.click()

browser.implicitly_wait(30)

compose = browser.find_element_by_css_selector('#\:lg > div > div')
compose.click()

browser.implicitly_wait(10)

sending = browser.find_element_by_xpath('//*[@id=":r0"]')
sending.send_keys(reciever)

browser.implicitly_wait(15)

subject = browser.find_element_by_xpath('//*[@id=":qi"]')
subject.send_keys('It is not me, AI it is.') #Write a subject to your email.

browser.implicitly_wait(25)

send = browser.find_element_by_xpath('//*[@id=":q8"]')
send.click()

browser.implicitly_wait(20)

browser.close()


