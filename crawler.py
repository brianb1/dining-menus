#!/usr/bin/python

import re
import requests
from bs4 import BeautifulSoup

html = requests.get("http://menu.ha.ucla.edu/foodpro/default.asp")
soup = BeautifulSoup(html.text, "html.parser")
cell_types = ["menugridcell", "menugridcell_last"]

for table in soup.find_all(class_="menugridtable"):
    try:
        print(table.find(class_="menumealheader").contents[0].strip() + ":")
    except:
        pass
    halls = table.find_all(class_="menulocheader")
    for i in range(0,2):
        print('\t' + halls[i].string)
        for cell in table.find_all(class_=cell_types[i]):
            print("\t\t" + cell.li.string)
            for item in cell.find_all(class_=re.compile("^itemlink")):
                print("\t\t\t" + item.string)
