__author__="Ryan Gavin"
__date__ ="$Dec 7, 2010 11:14:29 PM$"

import oauth2 as oauth

def __init__():
	#set up oauth
	consumer = oauth.Consumer(key='9c528f5ba470e0da2dcdc72ae12318f704d8d2da3',secret='97b58cafaff8335942ae5da08712c4ec')
	client = oauth.Client(consumer)

def searchEntities(entityName)
	url = 'http://qa.generalsentiment.com:8080/api/v1/searchEntities?entityName='
	entityName.replace(' ','%20")
	url = url+entityName
	method= 'GET'
	response,content = client.request(url,method)
	return content

def getSentiment(entityName, startDate, endDate):
	url = 'http://qa.generalsentiment.com:8080/api/v1/getSentiment?entityName='
	entityName.replace(' ','%20")
	url = url+entityName+'&'+'startDate'+startDate+'&'+endDate'
	method= 'GET'
	response,content = client.request(url,method)
	return content
	
def getJuxta(entityName, startDate, endDate):
	url = 'http://qa.generalsentiment.com:8080/api/v1/getJuxta?entityName='
	entityName.replace(' ','%20")
	url = url+entityName+'&'+'startDate'+startDate+'&'+endDate'
	method= 'GET'
	response,content = client.request(url,method)
	return content