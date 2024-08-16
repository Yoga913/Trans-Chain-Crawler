import requests
# berfungsi melakukan peminataan respons url
def requester(url):
	return requests.get('https://blockchain.info/rawaddr/' + url).text