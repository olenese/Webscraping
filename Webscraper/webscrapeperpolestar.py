from selenium import webdriver
import smtplib

url = 'https://hotell.difi.no/?dataset=vegvesen/kjoretoy&query=JM1NA3512M1221038'
browser = webdriver.Chrome("/Users/olenese/Programmering/Python/Webscraper/chromedriver")
browser.get(url)

browser.find_element_by_xpath('//*[@id="data"]/div[3]/table/tbody/tr/td[5]')

##https://hotell.difi.no/?dataset=vegvesen/kjoretoy&query=LPSVSEDEEML014003
