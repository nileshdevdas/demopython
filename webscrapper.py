from bs4 import  BeautifulSoup;
from urllib  import request;
import re;
data = request.urlopen('https://www.amazon.in/');
soup = BeautifulSoup(data , features="html.parser")
title = soup.title;
print(soup.head)
print(soup.body)
print(title)
print(soup.find("div", {"class": "a-cardui-header"}));

# mysql, postgres, mssql, Cx_oracle,
# urllib
# base64
# bs4


