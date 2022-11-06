import os
import time

from study import study

username=["13368229942"] #手机号 https://m.bjyouth.net/site/login
password=["songyixin2000"]
ua = os.getenv('UA',
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42')

succList = []
for i in range(0,len(username)):
    if study(username[i], password[i], ua):
        succList.append(username[i])

print("成功list:",succList)
