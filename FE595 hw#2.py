import requests
import bs4
from numpy import arange


index=list()
for i in range(0,50):
    web = requests.get('http://3.95.249.159:8000/random_company')
    web = web.text
    soup = bs4.BeautifulSoup( web,'html.parser')
    for x in soup.find_all('li'):
        x=x.text.split(':')
        if x[0]=='Name':
            index.append(x)
        if x[0]=='Purpose':
            index.append(x)
    

name=index[1::4]
purpose=index[3::4]
with open("output.txt",'w') as out_file:
    for t in range(len(index)):
        res=""
        res += str(index[t])
        res += "\n"
        out_file.write(res)
