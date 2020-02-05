import requests
import random
from bs4 import BeautifulSoup

f = open('ip_addresses.txt','r')
ip_addresses = eval(f.read())
f.close()
ip_failed = []

def getw(ip,ip_addresses):

	if ip !="" : ip_addresses.append(ip)
	pi = random.randint(0, len(ip_addresses) - 1)
	URL = 'http://free-proxy.cz/en/'
	
	proxies = {"http":ip_addresses[pi],"https":ip_addresses[pi]}

	s = requests.Session()
	try : 
		page = s.get(URL,proxies=proxies,timeout=5)
		return page,pi
	except:
		return 1,pi
ip = ""
for i in range(10):
	try:	
		page,pi = getw(ip,ip_addresses)
		if  page ==1 : raise Exception()
	except:
		print("Error Ocurred Retrying after attempt ",i+1)
	
		ip_failed.append(ip_addresses.pop(pi))
		print(str(ip_failed))
		if i==9:
		  ip = str(input("Enter the new IP: "))
		  i = 8
	else:
		break

soup = BeautifulSoup(page.content,features="html.parser")

html = soup.find_all(class_='left')

for i in list(html):
    print('\n\n',i.text)