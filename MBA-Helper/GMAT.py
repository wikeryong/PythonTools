
#!/usr/bin/env python
#coding:utf-8
import requests
import re
from bs4 import BeautifulSoup
import time
from urllib import urlencode

#print 111;




def req_html(ksrq=''):
	url = 'https://registration.mba.com/testtaker/registration/CalendarAppointmentSearchPage/GMAC'
	resp = requests.get(url, verify=True)
	#soup = BeautifulSoup(resp.content)
	print resp.content
	


