import urllib2
import cookielib
import urllib
import re

cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)

p= raw_input("Please input the PinYing of your Province:")
c= raw_input("Please input the PinYing of your City:")

url="http://www.51hao.cc/city/"+p+"/"+c+".php"
request = urllib2.Request(url)
response = opener.open(request)
html_a = response.read()

#print html_a,cookie

result=re.findall(u"1[358][0-9]{5}",html_a)
section = list(set(result))
section.sort(key=result.index)

mantissa=[]

for i in range(10000):
    if i< 10:
        mantissa.append("000"+str(i))
    elif i<100:
        mantissa.append("00"+str(i))
    elif i<1000:
        mantissa.append("0"+str(i))
    else:
        mantissa.append(str(i))

f = open(c+'.txt', 'w')
for a in section:
    for b in mantissa:
        f.write(a+b+"\n")
f.close()
print "dictionary has been finished!"
