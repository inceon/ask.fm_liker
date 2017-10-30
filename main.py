import requests
import yaml
import sys
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime
from random import *
from pprint import pprint
from time import sleep

indexPage = 'https://ask.fm/'
TL = 80
DT = 6
R = 30

def get_users_on_index():
	r = requests.get(indexPage)
	soup = BeautifulSoup(r.text, "html.parser")

	users = []

	# Parse users name
	for td in soup.findAll("nav", class_="faces"):
	    for a in td.findAll("a", href=True)[1:]:
	        users.append(a.text)

	return users

# pprint(indexPage + users[0])
# Open browser
browser = webdriver.PhantomJS()

stream = open('cookie.data', 'r')
cookie = yaml.load(stream)

browser.get(indexPage)
browser.delete_all_cookies()
browser.add_cookie(cookie)

def like_answer():
	users = get_users_on_index()
	for i in users:
		pprint(i)
		browser.get(indexPage + i)
		sleep(DT)
		browser.find_element_by_xpath('//*[@id="contentArea"]/div[2]/div[1]/div[4]/div/div[1]/div[4]/div/a[1]').click()
		pprint('first like')
		sleep(DT)
		browser.find_element_by_xpath('//*[@id="contentArea"]/div[2]/div[1]/div[4]/div/div[2]/div[4]/div/a[1]').click()
		pprint('second like')
		sleep(DT)
		with open("like_login.txt", "a") as f:
			f.write(str(i)+'\n')


while True:
	try:
		like_answer()
	except:
		print(datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S") + '\tinceon\tUnexpected error: '+str(sys.exc_info()[0]))
	
	sleep(randint(-R, R) + TL)
