#!/usr/bin/python3

#NOT MY CODE
#Engineer Man
#9/23/2018
#py script
#source code
#https://www.facebook.com/engineermanyt

import requests
import re

# get the data
data = requests.get('http://www.mg-cc.org/club-information/club-contacts')

# extract the phone numbers, emails, whatever
phones = re.findall(r'(\(?[0-9]{3}\)?(?:\-|\s|\.)?[0-9]{3}(?:\-|\.)[0-9]{4})', data.text)
emails = re.findall(r'([\d\w\.]+@[\d\w\.\-]+\.\w+)', data.text)

print(phones, emails)