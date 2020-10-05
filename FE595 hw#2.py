import requests
import bs4
from numpy import arange
import time

index = list()
class webscapper():
    for i in range(0,50):
        try:
            web = requests.get('http://3.95.249.159:8000/random_company')
            web = web.text
            soup = bs4.BeautifulSoup( web,'html.parser')
            for x in soup.find_all('li'):
                x=x.text.split(':')
                if x[0]=='Name':
                    index.append(x)
                if x[0]=='Purpose':
                    index.append(x)
        except:
            index = ["error"]

    name=index[1::4]
    purpose=index[3::4]
    with open("output.txt",'w') as out_file:
        for t in range(len(index)):
            res=""
            res += str(index[t])
            res += "\n"
            out_file.write(res)
            time.sleep(1)

