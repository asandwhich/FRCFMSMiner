#THIS OUTPUTS A DATA.JS FILE IN THE SAME DIRECTORY AS THE SCRIPT
#CLEARLY, THIS IS INTENDED TO BE RUN ON A CRONJOB OR SOME SUCH NONSENSE

import urllib2
from string import replace
from bs4 import BeautifulSoup
import json

teamq = {}
teamqp = {}
teamp = {}

page = urllib2.urlopen("http://www2.usfirst.org/2013comp/Events/NHMA/rankings.html")
soup = BeautifulSoup(page.read())

temp = soup.body
temp = temp.find_all('table')[2]
row = temp.find_all('tr')[2]

while row != None:
	data = row.contents
	teamq[unicode(data[3].contents[0])]=[float(unicode(data[5].contents[0])),float(unicode(data[7].contents[0]))]
	teamqp[unicode(data[3].contents[0])]=[float(), float(unicode(data[5].contents[0])), float(unicode(data[19].contents[0]))]
	teamp[unicode(data[3].contents[0])]=[float(), float(unicode(data[19].contents[0]))]
	row = row.next_sibling.next_sibling

page = urllib2.urlopen("http://www2.usfirst.org/2013comp/Events/NHMA/matchresults.html")
soup = BeautifulSoup(page.read())

temp = soup.body

temp = temp.find_all('table')[2]
row = temp.find_all('tr')[3]

while row != None:
	data = row.contents
	teamqp[unicode(data[5].contents[0])][0] += float(unicode(data[17].contents[0]))
	teamqp[unicode(data[7].contents[0])][0] += float(unicode(data[17].contents[0]))
	teamqp[unicode(data[9].contents[0])][0] += float(unicode(data[17].contents[0]))
	teamqp[unicode(data[11].contents[0])][0] += float(unicode(data[19].contents[0]))
	teamqp[unicode(data[13].contents[0])][0] += float(unicode(data[19].contents[0]))
	teamqp[unicode(data[15].contents[0])][0] += float(unicode(data[19].contents[0]))
	teamp[unicode(data[5].contents[0])][0] += float(unicode(data[17].contents[0]))
	teamp[unicode(data[7].contents[0])][0] += float(unicode(data[17].contents[0]))
	teamp[unicode(data[9].contents[0])][0] += float(unicode(data[17].contents[0]))
	teamp[unicode(data[11].contents[0])][0] += float(unicode(data[19].contents[0]))
	teamp[unicode(data[13].contents[0])][0] += float(unicode(data[19].contents[0]))
	teamp[unicode(data[15].contents[0])][0] += float(unicode(data[19].contents[0]))
	row = row.next_sibling.next_sibling

for key in teamqp:
	teamqp[key][0] /= teamqp[key][2]

for key in teamp:
	teamp[key][0] /= teamp[key][1]

f = open('data.js', 'w')
f.write("var teamq = ")
f.write(replace(replace(replace(replace(json.dumps(teamq, indent=1),'\": [', ','), '\"', '['), '{', '['), '}', ']'))
f.write("\n\n")

f.write("var teamqp = ")
f.write(replace(replace(replace(replace(json.dumps(teamqp, indent=1),'\": [', ','), '\"', '['), '{', '['), '}', ']'))
f.write("\n\n")

f.write("var teamp = ")
f.write(replace(replace(replace(replace(json.dumps(teamp, indent=1),'\": [', ','), '\"', '['), '{', '['), '}', ']'))
f.close()
