# Author: All I Do Is Ace
import requests
import json

# Insert your Riot API key.
riotKey = ''

# Checks the code status of request & calls codeCatcher if not successful request
def codeCheck(c):
	c = c.status_code
	if c == 200:
		return True
	else:
		codeCatcher(c)
		return False

def codeCatcher(errorCode):
	if errorCode == 400:
		print('Please enter a different Summoner\'s Name...')
	elif errorCode == 401:
		print('Unauthorized request, please try again...')
	elif errorCode == 404:
		print('There is currently no data for this Summoner...')
	elif errorCode == 429:
		print('The rate limit has been exceeded, please try again...')
	elif errorCode == 500 or errorCode == 503:
		print('Oops, service is unavailable...')
	return errorCode

# Function for Uppercase to Lowercase
def upperToLower(r):
	r = str(r)
	r.lower()
	return r

def regionEval(r):
	regionProd = True
	if r in ('na', 'north america', 'northamerica'):
		r = 'na'
	elif r in ('br', 'brazil'):
		r = 'br'
	elif r in ('eune', 'europe nordic and east', 'europe nordic & east', 'europenordicandeast', 'europenordic&east'):
		r = 'eune'
	elif r in ('euw', 'europe west', 'europewest'):
		r = 'euw'
	elif r in ('lan', 'latin america north', 'latinamericanorth'):
		r = 'lan'
	elif r in ('las', 'latin america south', 'latinamericasouth'):
		r = 'las'
	elif r in ('oce', 'oceania'):
		r = 'oce'
	elif r in ('ru', 'russia'):
		r = 'ru'
	elif r in ('tr', 'turkey'):
		r = 'tr'
	elif r in ('jp', 'japan'):
		r = 'jp'
	elif r in ('sea', 'south east asia', 'southeastasia'):
		r = 'sea'
	elif r in ('kr', 'republic of korea', 'republicofkorea'):
		r = 'kr'
	elif r in ('pbe', 'public beta environment', 'publicbetaenvironment'):
		r = 'pbe'
	else:
		regionProd = False
	return r, regionProd

# Gets basic summoner info.
def summonerInfo(region, regionProd):
	typedSumName = str(input('Please type the Summoner\'s Name: '))
	searchSumName = typedSumName.replace(' ','')

	thisURL = 'https://' + region + '.api.pvp.net/api/lol/' + region + '/v1.4/summoner/by-name/' + searchSumName + '?api_key=' + riotKey

	response = requests.get(thisURL)
	data = response.json()
	codeStatus = codeCheck(response)

	if codeStatus == True:
		actualSumName = str(data[searchSumName]['name'])
		summonerID = str(data[searchSumName]['id'])
		summonerLevel = str(data[searchSumName]['summonerLevel'])
	else:
		print('Please try a different Summoner Name or Region')
		summonerInfo()
	return actualSumName, summonerID, summonerLevel

# # # # # # # # # # # # # # # # #
# Beginning of Running Program  #
# # # # # # # # # # # # # # # # #
region = upperToLower(input('Please type a region (ie. NA): '))
region, regionProd = regionEval(region)

if regionProd == True:
	# Puts the return values of summonerInfo() into the respective variables
	actualSumName, summonerID, summonerLevel = summonerInfo(region, regionProd)
else:
	print('There was an error with your search.')

print('Summoner\'s Name: ' + actualSumName)
print('Summoner\'s ID: ' + summonerID)
print('Summoner\'s Level: ' + summonerLevel)

