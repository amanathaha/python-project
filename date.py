import datetime 
print(datetime.date.today())

import os
print(os.listdir())

import json
data = {"name": "John", "age": 20}
print(json.dumps(data))

import re
text = "My age is 20"
print(re.findall(r"\d+", text))

from collections import Counter
fruits = ["apple", "apple", "banana"]
print(Counter(fruits))

import sys
print(sys.version)