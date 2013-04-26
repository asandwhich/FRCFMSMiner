#THIS OUTPUTS A DATA.JS FILE IN THE SAME DIRECTORY AS THE SCRIPT
#CLEARLY, THIS IS INTENDED TO BE RUN ON A CRONJOB OR SOME SUCH NONSENSE

from urllib.request import *
from bs4 import *
import json

teamq = {}
teamqp = {}
teamp = {}

page = urlopen("http://www2.usfirst.org/2013comp/Events/ARFA/rankings.html")
soup = BeautifulSoup(page.read())

temp = soup.body
temp = temp.find_all('table')[2]
row = temp.find_all('tr')[2]

while row != None:
	data = row.contents
	teamq[data[3].contents[0]]=[float(data[5].contents[0]),float(data[7].contents[0])]
	teamqp[data[3].contents[0]]=[float(), float(data[5].contents[0]), float(data[19].contents[0])]
	teamp[data[3].contents[0]]=[float(), float(data[19].contents[0])]
	row = row.next_sibling.next_sibling

page = urlopen("http://www2.usfirst.org/2013comp/Events/ARFA/matchresults.html")
soup = BeautifulSoup(page.read())

temp = soup.body

temp = temp.find_all('table')[2]
row = temp.find_all('tr')[3]

while row != None:
	data = row.contents
	teamqp[data[5].contents[0]][0] += float(data[17].contents[0])
	teamqp[data[7].contents[0]][0] += float(data[17].contents[0])
	teamqp[data[9].contents[0]][0] += float(data[17].contents[0])
	teamqp[data[11].contents[0]][0] += float(data[19].contents[0])
	teamqp[data[13].contents[0]][0] += float(data[19].contents[0])
	teamqp[data[15].contents[0]][0] += float(data[19].contents[0])
	teamp[data[5].contents[0]][0] += float(data[17].contents[0])
	teamp[data[7].contents[0]][0] += float(data[17].contents[0])
	teamp[data[9].contents[0]][0] += float(data[17].contents[0])
	teamp[data[11].contents[0]][0] += float(data[19].contents[0])
	teamp[data[13].contents[0]][0] += float(data[19].contents[0])
	teamp[data[15].contents[0]][0] += float(data[19].contents[0])
	row = row.next_sibling.next_sibling

for key in teamqp:
	teamqp[key][0] /= teamqp[key][2]

for key in teamp:
	teamp[key][0] /= teamp[key][1]

f = open('data.js', 'w')
f.write("var teamq = ")
f.write(json.dumps(teamq, indent=1).replace('\": [', ',').replace('\"', '[').replace('{', '[').replace('}', ']'))
f.write("\n\n")

f.write("var teamqp = ")
f.write(json.dumps(teamqp, indent=1).replace('\": [', ',').replace('\"', '[').replace('{', '[').replace('}', ']'))
f.write("\n\n")

f.write("var teamp = ")
f.write(json.dumps(teamp, indent=1).replace('\": [', ',').replace('\"', '[').replace('{', '[').replace('}', ']'))
f.close()
