#!/usr/bin/python

import re
from bs4 import BeautifulSoup

soup = BeautifulSoup(open("default.asp", encoding="ISO-8859-1"), "html.parser")
cell_types = ["menugridcell", "menugridcell_last"]

for table in soup.find_all(class_="menugridtable"):
    try:
        print(table.find(class_="menumealheader").contents[0].strip())
    except:
        pass
    halls = table.find_all(class_="menulocheader")
    for i in range(0,2):
        print('\t' + halls[i].string)
        for cell in table.find_all(class_=cell_types[i]):
            try:
                print("\t\t" + cell.li.string)
            except:
                print("\t\tThe Grill")
            for item in cell.find_all(class_=re.compile("^itemlink")):
                print("\t\t\t" + item.string)
