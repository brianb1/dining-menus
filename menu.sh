#!/bin/sh

wget -q http://menu.ha.ucla.edu/foodpro/default.asp
python ~/projects/dining-menus/crawler.py
rm default.asp
