# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 01:27:23 2023

@author: admin
"""

import requests
import json
resp = requests.get('http://34.81.147.202:7878/num/8857619120,8857515096,8857515100,8706648436,8706774650')

decode =json.loads(resp.content)

print (decode)
