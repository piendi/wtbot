#!/usr/bin/python
# -*- coding: utf8 -*-
"""
WEB TRAFFIC BOT 0.0.1
(C) 2017 Sojuniter 
sojuniter@gmail.com
H4CK THE PLANET

"""
import urllib2 
import urllib
import sys
import time
import random
import re
import os
print """
######################################################################
#--> WTBOT - Web Traffic Bot 0.0.1                                <--#
#--> proudly presented by Sojuniter                               <--#
#--> H4CK THE PLANET                                              <--#
######################################################################
"""
print ""
print ""
proxylisttext = raw_input("--> Path to your Proxylist file: ")
"""
useragent section - Deceive the web host to be a browser from the list of user agents. 
					Important not to be recognized as a bot. 
"""

useragent = ['Mozilla/4.0 (compatible; MSIE 5.0; SunOS 5.10 sun4u; X11)',
		   'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.2pre) Gecko/20100207 Ubuntu/9.04 (jaunty) Namoroka/3.6.2pre',
		   'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser;',
		   'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0)',
		   'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1)',
		   'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.6)',
		   'Microsoft Internet Explorer/4.0b1 (Windows 95)',
		   'Opera/8.00 (Windows NT 5.1; U; en)',
		   'amaya/9.51 libwww/5.4.0',
		   'Mozilla/4.0 (compatible; MSIE 5.0; AOL 4.0; Windows 95; c_athome)',
		   'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
		   'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
		   'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; ZoomSpider.net bot; .NET CLR 1.1.4322)',
		   'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; QihooBot 1.0 qihoobot@qihoo.net)',
           'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:2.0) Treco/20110515 Fireweb Navigator/2.4',
           'Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; XH; rv:8.578.498) fr, Gecko/20121021 Camino/8.723+ (Firefox compatible)',
           'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
           'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:2.0) Treco/20110515 Fireweb Navigator/2.4',
           'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246',
           'IBM WebExplorer /v0.94',
           'Mozilla/5.0 (Macintosh; PPC Mac OS X 10_5_8) AppleWebKit/537.3+ (KHTML, like Gecko) iCab/5.0 Safari/533.16',
           'Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20121202 Firefox/17.0 Iceweasel/17.0.1',
           'Lynx/2.8.8dev.3 libwww-FM/2.14 SSL-MM/1.4.1',
           'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2.3) Gecko/20100402 Prism/1.0b4',
           'Mozilla/5.0 (Macintosh; PPC Mac OS X 10.5; rv:10.0.2) Gecko/20120216 Firefox/10.0.2 TenFourFox/7450',
		'Mozilla/4.0 (compatible; MSIE 5.0; Windows ME) Opera 5.11 [en]']

referer	= ['http://google.com','http://bing.com','http://facebook.com','http://twitter.com','http://ask.com','http://baidu.com','http://m.facebook.com','http://m.facebook.de','http://instagram.de','http://youtube.de','http://ebay.de','http://amazon.de','http://zalando.de','http://blogspot.de','http://www.abacho.de','http://acoon.de','http://www.bellnet.com','http://www.apollo7.de','http://www.bigfoot.com','http://www.altavista.com','http://www.blitzsuche.de','http://www.cnet.com','http://www.goto.com','http://www.greenseek.de','http://www.excite.de','http://netguide.de','http://www.search11.ch','http://www.conrad.de','http://yellow.com',"http://www.suchen.de",'http://ask.fm','http://sharelook.de']
link_invation = raw_input("--> Link to Autovisit (Full URL with http:// or https://): ")

def bot(proxy1):
    try:
	proxy = proxy1.split(":")
        print 'Auto Click Using proxy :',proxy1
	proxy_set = urllib2.ProxyHandler({"http" : "%s:%d" % (proxy[0], int(proxy[1]))})
	opener = urllib2.build_opener(proxy_set, urllib2.HTTPHandler)
	opener.addheaders = [('User-agent', random.choice(useragent)),
						('Referer', random.choice(referer))]
	urllib2.install_opener(opener)
	f = urllib2.urlopen(link_invation)
	if link_invation in f.read():
	   print "[*] Link Visited ..."
	else:
	   print "[*] Link Visit Failed -Ops- !"
           print "[!] Proxy failed"

    except:
           print "[!] Proxy Error "
           pass

def loadproxy():
    try:
	get_file = open(proxylisttext, "r")
	proxylist = get_file.readlines()
	count = 0
        proxy = []
	while count < len(proxylist):
	      proxy.append(proxylist[count].strip())
	      count += 1
        for i in proxy:
            bot(i)
    except IOError:
	print "\n[-] Error: Check your proxylist path\n"
	sys.exit(1)

def main():
   loadproxy()
if __name__ == '__main__':
	main()
