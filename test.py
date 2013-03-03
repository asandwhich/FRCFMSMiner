#THIS OUTPUTS A DATA.JS FILE IN THE SAME DIRECTORY AS THE SCRIPT
#CLEARLY, THIS IS INTENDED TO BE RUN ON A CRONJOB OR SOME SUCH NONSENSE

import urllib2
from string import replace
from bs4 import BeautifulSoup
import json

teams = {}

page = urllib2.urlopen("http://www2.usfirst.org/2013comp/Events/NHMA/rankings.html")
soup = BeautifulSoup(page.read())

temp = soup.body
temp = temp.find_all('table')[2]
row = temp.find_all('tr')[2]

while row != None:
	data = row.contents
	teams[unicode(data[3].contents[0])]=[float(), float(unicode(data[5].contents[0])),float(unicode(data[7].contents[0])),float(unicode(data[9].contents[0])),float(unicode(data[11].contents[0])),float(unicode(data[13].contents[0])),float(unicode(data[17].contents[0])),float(unicode(data[19].contents[0]))] 
	row = row.next_sibling.next_sibling

page = urllib2.urlopen("http://www2.usfirst.org/2013comp/Events/NHMA/matchresults.html")
soup = BeautifulSoup(page.read())

temp = soup.body

temp = temp.find_all('table')[2]
row = temp.find_all('tr')[3]

while row != None:
	data = row.contents
	teams[unicode(data[5].contents[0])][0] += float(unicode(data[17].contents[0]))
	teams[unicode(data[7].contents[0])][0] += float(unicode(data[17].contents[0]))
	teams[unicode(data[9].contents[0])][0] += float(unicode(data[17].contents[0]))
	teams[unicode(data[11].contents[0])][0] += float(unicode(data[19].contents[0]))
	teams[unicode(data[13].contents[0])][0] += float(unicode(data[19].contents[0]))
	teams[unicode(data[15].contents[0])][0] += float(unicode(data[19].contents[0]))
	row = row.next_sibling.next_sibling

for key in teams:
	teams[key][0] /= teams[key][7]

f = open('data.js', 'w')
f.write(replace(replace(replace(replace(json.dumps(teams, indent=1),'\": [', ','), '\"', '['), '{', '['), '}', ']'))
f.close()
