#more URLs at http://pastebin.com/v8KGi8v0
"""
When using this product. Please remember to give credit to oni49, 
the author of this product. 

Reachable at Twitter @oni_49 and GitHub @oni49. Feedback welcome.
"""
try:
	from TorCtl import TorCtl
except Exception, e:
	print "[!] Error loading TorCTL"
import urllib2, time

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers={'User-Agent':user_agent}

def set_urlproxy():
	proxy_support = urllib2.ProxyHandler({"http" : "127.0.0.1:8118"})
	opener = urllib2.build_opener(proxy_support)
	opener.addheader = [('User-agent', user_agent)]
	urllib2.install_opener(opener)

def request(url):
#	def _set_urlproxy():
#		proxy_support = urllib2.ProxyHandler({"http" : "127.0.0.1:8118"})
#		opener = urllib2.build_opener(proxy_support)
#		opener.addheader = [('User-agent', user_agent)]
#		urllib2.install_opener(opener)
#	_set_urlproxy()
	request=urllib2.Request(url, None, headers)
	return urllib2.urlopen(request).read()

def header_only(url):
	request=urllib2.Request(url, None, headers)
	return urllib2.urlopen(request).getcode()

def renew_connection():
	conn = TorCtl.connect(controlAddr="127.0.0.1", controlPort=9051, passphrase="password") #use a better password than this
	conn.send_signal("NEWNYM")
	conn.close()
	print "Waiting for connection to renew"
	time.sleep(10) #added so it could finish drawing new circuit before next step

set_urlproxy()
renew_connection()
print "Current IP:", request("http://icanhazip.com/")

targetFile = open('tabDel.txt', 'r')
targetLines = targetFile.readlines()
goodSites = open('code200sites.txt', 'w')

count = 0
for line in targetLines:
	splits = line.strip('\n').split('\t')
	site = splits[1][0:30]+'/server-status'
	try:
		code = header_only(site)
		#print site
		#code = 0
		goodSites.write(str(code)+'\t'+splits[0]+'\t'+site+'\n')
	except Exception, e:
		print site, e
	count = count + 1
	if count % 15 == 0:
		renew_connection()
		print "Current IP:", request("http://icanhazip.com/")

