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
	URL = 'http://www.tamilrockers.ws'
	
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
soup = BeautifulSoup(page.content, 'html.parser')

result = soup.find_all('div', class_='ipsType_textblock ipsPad')


res = result[0].find_all('span')

def search(movie):
	for i in range(0,len(list(res))):
		if movie in res[i].text:

			if len(res[i]) < 30 :
				print(res[i].text)		
				size = str(input('Enter the Desired size: '))
				if size != '' and size in res[i].text:
					link = res[i].find_all('a')
					print(res[i])
					print(link)
			else:
				pos = res[i].text.find(movie)
				print("Pos:",pos,res[i].text[pos:pos+50])


def url():
	elems = soup.find_all('a', class_='bbc_url')

	print(len(elems))

	for i in range(len(elems)):
		print(elems[i].text)
while True:
   movie = str(input("Search for New movie :"))
   if movie == "": break
   search(movie)

f = open('ip_failed.txt','a')
f.write(str(ip_failed))
if len(ip_failed)>0: 
	f = open("ip_addresses.txt",'w')
	f.write(str(ip_addresses)) 