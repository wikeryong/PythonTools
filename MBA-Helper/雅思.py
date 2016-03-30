
#!/usr/bin/env python
#coding:utf-8
import requests
import re
from bs4 import BeautifulSoup
import time
from urllib import urlencode

#print 111;


TD_NAME={
	0:'考试日期',
	1:'考试类型',
	2:'考试类别',
	3:'省份',
	4:'城市',
	5:'考点名称',
	6:'截止及查询寄送日期',
	7:'',
	#8:'考试日期',
}
#print r.content

def write_txt(txt):
	file_object = open('list.html', 'a')
	file_object.write(txt)
	file_object.close()


def req_html(ksrq=''):
    url = 'https://www.chinaielts.org/apply/ielts_test_centres.shtml?kslx=%E9%9B%85%E6%80%9D%E8%80%83%E8%AF%95&ksrq='+ksrq+'&chengshi=上海#dataList'
    resp = requests.get(url, verify=True)
    soup = BeautifulSoup(resp.content)
    table = soup.find('table')
    tr_arr = table.find_all('tr')
    for tr in tr_arr:
        write_txt('<tr>')
        td_arr = tr.find_all('td')
        i=0
        for td in td_arr:
            if i==7:
                continue
            if i==4:
                write_txt('<td>'+td.text.encode('utf-8')+'</td>')
            if i==5:
            	write_txt('<td>'+td.text.encode('utf-8')+'</td>')
            if i==0:
            	write_txt('<td>'+td.text.encode('utf-8')+'</td>')
            i+=1;
        #print '----------------------------------------------------'
        write_txt('</tr>')


'''
r = requests.get('https://www.chinaielts.org/apply/ielts_test_centres.shtml?kslx=%E9%9B%85%E6%80%9D%E8%80%83%E8%AF%95&ksrq=10/29/2016&chengshi=%E4%B8%8A%E6%B5%B7#dataList', verify=True)
soup = BeautifulSoup(r.content)
table = soup.find('table')
tr_arr = table.find_all('tr')
for tr in tr_arr:
	td_arr = tr.find_all('td')
	i=0
	for td in td_arr:
		if i==7:
			continue
		write_txt(TD_NAME.get(i)+" : "+td.text.encode('utf-8')+'\n')
		i+=1;
	write_txt('----------------------------------------------------------------\n')
	write_txt('\n')
	write_txt('\n')
	write_txt('\n')
	write_txt('\n')
#write_txt(soup.find('table').encode("gbk"))

'''

r = requests.get("https://www.chinaielts.org/cuser/getCxKsrq.php?kslx=%E9%9B%85%E6%80%9D%E8%80%83%E8%AF%95")
dataArr = eval(r.content)
write_txt('<table>')
for dd in dataArr:
    date = dd['ksrq'].replace('\\','')
    print date
    req_html(date)
    time.sleep(2)
write_txt('</table>')
	#print date
#print dataArr[2]['ksrq'].replace('\\','')
#print r.text
#print r.text.encode("utf-8")
