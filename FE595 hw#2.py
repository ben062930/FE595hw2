import requests
import bs4


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
    out_file.write(str(index))# so that the script will write to the disk just once, but I don't know how to change the row.
out_file.close()
