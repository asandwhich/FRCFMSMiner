import urllib2
import time
import sqlite3
from BeautifulSoup import BeautifulSoup
tweetVals = []

dbConn = sqlite3.connect('scoutingData.db')
dbCurs = dbConn.cursor()
dbCurs.execute('CREATE TABLE results ( MC int, RF int, BF int, RA1 int, RA2 int, RA3 int, BA1 int, BA2 int, BA3 int, RC int, BC int, RFP int, BFP int, RAS int, BAS int, RTS int, BTS int)' ) 


def writeOut( vals ):
	global dbCurs
	for value in vals:
		elements = value.split(' ')
		intlist = []
		for q in elements:
			try:
				intlist.append(int(q))
			except:
				pass
		dbCurs.execute('INSERT INTO results VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', intlist[:17])

def commitnClose():
	global dbCurs
	global dbConn
	dbConn.commit()
	dbConn.close()
while True:
	twitterPageUrl = urllib2.urlopen( "https://twitter.com/frcfms" )
	twitterPage = twitterPageUrl.read()
	twitterSoup = BeautifulSoup( twitterPage )
	tweets = twitterSoup.findAll('p',{'class':'js-tweet-text'})
	immediateVals = []
	for i in tweets:
		immediateVals.append(str(i.contents[1]))#tweetVals.append(str(i.contents[1]))

	toBeWritten = list( set(immediateVals) - set(tweetVals) )
	tweetVals = immediateVals
	if len( toBeWritten ) > 0 :
		writeOut(toBeWritten)
	commitnClose()
	time.sleep(60)
	break
	#print tweetVals

